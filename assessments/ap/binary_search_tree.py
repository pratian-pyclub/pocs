class Tree():
    def __init__(self, v):
        if self._valid(v):
            self.root = Node(v)

    def insert(self, v):
        if self._valid(v):
            self.root.insert(v)

    def display(self):
        self.root.display()

    def _valid(self, v):
        if type(v) is not int:
            raise Exception('Unsupported type. Please try again')
        else:
            return True

class Node():
    def __init__(self, v):
        self.v = v
        self.left = Empty()
        self.right = Empty()

    def insert(self, v):
        if v < self.v:
            self._insert_left(v)
        elif v > self.v:
            self._insert_right(v)

        return True

    def display(self):
        print "--- {0}".format(self.v)
        print "---L- {0}".format(self.left.v)
        print "---R- {0}".format(self.right.v)
        self.left.display()
        self.right.display()

    def _insert_left(self, v):
        if isinstance(self.left, Empty):
            self.left = Node(v)
        else:
            self.left.insert(v)

    def _insert_right(self, v):
        if isinstance(self.right, Empty):
            self.right = Node(v)
        else:
            self.right.insert(v)

class Empty():
    def __init__(self, v = "*"):
        self.v = v

    def display(self):
        return None

    def insert(self, v):
        return False

t = Tree(10)
t.insert(7)
t.insert(2)
t.insert(5)
t.insert(6)
t.insert(9)
t.insert(3)
t.insert(1)
t.insert(4)
t.display()
