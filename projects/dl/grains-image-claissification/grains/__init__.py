# Local imports
from brain import Brain
from dirpath import DIRPATH

GRAINS = [
            {"group": "chick-peas", "group_id": 0, "path": DIRPATH + "/data/chick-peas/"},
            {"group": "green-peas", "group_id": 1, "path": DIRPATH + "/data/green-peas/"},
            {"group": "rice", "group_id": 2, "path": DIRPATH + "/data/rice/"}
        ]

class Grain():
    def __init__(self):
        self.brain = Brain()

    def save(self, location):
        self.brain.save(file_name=location)

    def load(self, location):
        self.brain.load(file_name=location)

    def train(self):
        for grain in GRAINS:
            print("Training " + grain["group"])
            for name in range(1, 5):
                filepath = grain["path"] + str(name) + ".jpg"
                self.brain.add_image_to_train(filepath, grain["group_id"])

        self.brain.train()

    def test(self, filepath):
        return self.brain.classify(filepath)
