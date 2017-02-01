import os

PWDPATH = os.path.abspath(__file__)
apipath = os.path.dirname(PWDPATH)

POSPATH = os.path.dirname(apipath) + '/data/pos.yml'
NEGPATH = os.path.dirname(apipath) + '/data/neg.yml'
N_FEATURES = 200

# POSPATH = os.path.dirname(apipath) + '/data/pos_small.yml'
# NEGPATH = os.path.dirname(apipath) + '/data/neg_small.yml'
# N_FEATURES = 20