import re
import mysql
import pytest
from mysql.connector import Connect

HOST = 'localhost'
USER = 'root'
PSWD = 'root'
DBNAME = 'office'

MYSQL_CONNECTION = Connect(host=HOST,
                       user=USER,
                       passwd=PSWD,
                       db=DBNAME)

class Employee():
    TBNAME = 'employees'
    CNAMES = {
        'name': {'column': 'name', 'type': 'varchar(30)', 'rules': re.compile('^[a-zA-Z]{2,30}$')},
        'dob': {'column': 'dob', 'type': 'date', 'rules': re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')},
        'salary': {'column': 'salary', 'type': 'double', 'rules': re.compile('[0-9]{3,10}')}
    }

    MYSQL_CUR = MYSQL_CONNECTION.cursor()

    @classmethod
    def create_table(cls):
        Employee.MYSQL_CUR.execute("create table {0}(".format(Employee.TBNAME) + \
        "id int primary key auto_increment," + \
        "{0} {1},".format(Employee.CNAMES['name']['column'], Employee.CNAMES['name']['type']) + \
        "{0} {1},".format(Employee.CNAMES['dob']['column'], Employee.CNAMES['dob']['type']) + \
        "{0} {1});".format(Employee.CNAMES['salary']['column'], Employee.CNAMES['salary']['type']))

    @classmethod
    def use_table(cls):
        Employee.MYSQL_CUR.execute("use {0};".format(DBNAME))

    @classmethod
    def fetch(cls, id):
        query = "select * from {0} where id = {1}".format(Employee.TBNAME, id)
        return Employee.MYSQL_CUR.execute(query)

    def __init__(self, name, dob, salary):
        self._validate_name(name)
        self._validate_dob(dob)
        self._validate_salary(salary)

    def insert(self):
        Employee.MYSQL_CUR.execute(self.__insert_db())
        MYSQL_CONNECTION.commit()
        self.__id = Employee.MYSQL_CUR.lastrowid

    def __insert_db(self):
        return "insert into {0} ".format(Employee.TBNAME) + \
        "({0}, {1}, {2}) ".format(Employee.CNAMES['name']['column'], Employee.CNAMES['dob']['column'], Employee.CNAMES['salary']['column']) + \
        "values ('{0}', '{1}', {2});".format(self.name, self.dob, self.salary)

    def _validate_name(self, name):
        if (Employee.CNAMES['name']['rules'].search(name) is not None):
            self.name = name
        else:
            raise ValueError("Unaccepted name format.")

    def _validate_dob(self, dob):
        if (Employee.CNAMES['dob']['rules'].search(dob) is not None):
            self.dob = dob
        else:
            raise ValueError("Unaccepted DOB format.")

    def _validate_salary(self, salary):
        if (Employee.CNAMES['salary']['rules'].search(str(salary)) is not None):
            self.salary = salary
        else:
            raise ValueError("Unaccepted salary format.")


# Employee.create_table()
Employee.use_table()

def test_valid_name():
    with pytest.raises(ValueError):
        e = Employee("Pr1ya", "1980-10-22", 48000)

def test_valid_date():
    with pytest.raises(ValueError):
        e = Employee("Priya", "19808-10-22", 48000)

def test_valid_salary():
    with pytest.raises(ValueError):
        e = Employee("Priya", "1980-10-22", 480000000000000000000)

def test_insert():
    e = Employee("Priya", "1980-10-22", 48000)
    e.insert()
    assert isinstance(e.__id, int)
