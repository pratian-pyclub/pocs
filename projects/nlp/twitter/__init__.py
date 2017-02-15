import pandas as pd
import yaml

from classifier import NBClassifier, POSPATH, NEGPATH

def load_file():
    with open(POSPATH, 'r') as f:
        df = pd.io.json.json_normalize(yaml.load(f))
    with open(NEGPATH, 'r') as f:
        df = df.append(pd.io.json.json_normalize(yaml.load(f)), ignore_index=True)

    return df

class TwiNalysis():
    def __init__(self):
        self.df = load_file()
        self.dates = self.df.date.unique()
        self.classifier = NBClassifier(load=True)

    # {
    #     (2017, 1, 11): {'neg': 8, 'pos': 1},
    #     (2017, 1, 12): {'neg': 10, 'pos': 9},
    #     (2017, 1, 13): {'neg': 9, 'pos': 5},
    #     (2017, 1, 14): {'neg': 14, 'pos': 27},
    #     (2017, 1, 15): {'neg': 16, 'pos': 16},
    #     (2017, 1, 16): {'neg': 6, 'pos': 9},
    #     (2017, 1, 17): {'neg': 14, 'pos': 11},
    #     (2017, 1, 18): {'neg': 74, 'pos': 39},
    #     (2017, 1, 19): {'neg': 198, 'pos': 92},
    #     (2017, 1, 20): {'neg': 378, 'pos': 1196}
    #     (2017, 1, 21): {'neg': 75, 'pos': 227},
    #  }
    def by_day(self):
        result = {}
        for date in self.dates:
            result[date] = {'pos': 0, 'neg': 0}
            for row in self.df.loc[self.df['date'] == date].itertuples():
                sent = self.classifier.classify(row.text)
                if sent == 'pos':
                    result[date]['pos'] += 1
                else:
                    result[date]['neg'] += 1

        return result

    # {
    #     'banjallikattu': {'neg': 608, 'pos': 327},
    #     'banpeta': {'neg': 194, 'pos': 1306}
    # }
    def by_hashtag(self):
        # 1 - banpeta
        # 0 - banjallikattu

        result = {
                    'banpeta': {'pos': 0, 'neg': 0},
                    'banjallikattu': {'pos': 0, 'neg': 0}
                }

        for row in self.df.itertuples():
            sent = self.classifier.classify(row.text)
            if row.sent == 1:
                if sent == 'pos':
                    result['banpeta']['pos'] += 1
                else:
                    result['banpeta']['neg'] += 1
            else:
                if sent == 'pos':
                    result['banjallikattu']['pos'] += 1
                else:
                    result['banjallikattu']['neg'] += 1

        return result
