import re 
sentence = 'i save tortur midnights torment native bull'

print bool(re.search('barbar?|ruthless',sentence, re.IGNORECASE))

