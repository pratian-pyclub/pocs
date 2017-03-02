import os

DIRPATH = os.path.dirname(os.path.abspath(__file__))
# HOMEPATH = os.path.expanduser("~")
HOMEPATH = DIRPATH + '/data'
MIFNAMES = ['id', 'name', 'release', 'url', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18']
MRANAMES = ['user_id', 'movie_id', 'rating', 'timestamp']

RATINGS_PATH = HOMEPATH + '/ratings.data'
UIX_PATH = HOMEPATH + '/uix.model'
MIX_PATH = HOMEPATH + '/mix.model'
INFO_PATH = HOMEPATH + '/info.data'

# from movrec import Movrec
# m = Movrec()
