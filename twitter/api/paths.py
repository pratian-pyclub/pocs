import os

PWDPATH = os.path.abspath(__file__)
apipath = os.path.dirname(PWDPATH)
POSPATH = os.path.dirname(apipath) + '/data/pos.yml'
NEGPATH = os.path.dirname(apipath) + '/data/neg.yml'
