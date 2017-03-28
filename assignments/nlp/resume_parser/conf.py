import os 
filepath = os.path.abspath(__file__)
PWDPATH = os.path.dirname(filepath)

LOC_FILE = 'location.txt'
LOC_PATH = os.path.join(PWDPATH, LOC_FILE)

STANFORD_NER = 'ner_tagger'
CLASSIFIER_FILE = 'classifiers/english.all.3class.distsim.crf.ser.gz'
JAR_FILE = 'stanford-ner.jar'

CLASSIFIER_PATH = os.path.join(PWDPATH, STANFORD_NER, CLASSIFIER_FILE)
JAR_PATH = os.path.join(PWDPATH, STANFORD_NER, JAR_FILE)