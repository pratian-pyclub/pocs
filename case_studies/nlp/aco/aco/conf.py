import os
import yaml

dirpath = os.path.dirname(os.path.abspath(__file__))
MAX_SIMILAR = 5
SHOWMATCH = True

CPTPATH = dirpath + "/data/cpt.yml"
with open(CPTPATH, 'r') as stream:
    try:
        CPTFILE = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

ICDPATH = dirpath + "/data/icd.yml"
with open(ICDPATH, 'r') as stream:
    try:
        ICDFILE = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
