#!/usr/bin/env python
"""

Brain class.

"""

import os
import sys
from sys import argv
import pickle

# PyBrain imports
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet, ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError
from pybrain import TanhLayer
from pybrain.structure.modules import SoftmaxLayer

# Local imports
import image_operations as io
from dirpath import HOMEPATH

def get_path(file_name):
    return HOMEPATH + "/" + file_name

class Brain():
    """
    Constructor.
    Input: hidden_nodes - number of hidden nodes used in the neuralnetwork
    """
    def __init__(self, hidden_nodes = 30):
        """
        parameters to buildNetwork are inputs, hidden layers, output
        bias = true allows for a bias unit to be added in each neural net layer
        hiddenclass represents the method used by the hidden layer
        """
        # Regression

        # self.classifier_neural_net = buildNetwork(12, hidden_nodes, 1, bias=True, hiddenclass=TanhLayer)
        # # Initializing dataset for supervised regression training
        # self.data_sets = SupervisedDataSet(12, 1)
        # # classification_trainer uses backpropagation supervised training method for training the newural network
        # self.classification_trainer = BackpropTrainer(self.classifier_neural_net, self.data_sets)

        # Classification
        self.classifier_neural_net = buildNetwork(12, hidden_nodes, 3, outclass=SoftmaxLayer, hiddenclass=TanhLayer)
        self.data_sets = ClassificationDataSet(12, 1, nb_classes=3)
        self.classification_trainer = BackpropTrainer(self.classifier_neural_net, self.data_sets, momentum=0.1, verbose=True, weightdecay=0.01)

    """
    Method to add a sample image to the datasets for training the classifier
    """
    def add_image_to_train(self, image_file, group_id):
        tto = io.twelve_tone(image_file)
        print(tto)
        # regression
        # self.data_sets.addSample(tto, (group_id,))

        # classification
        self.data_sets.addSample(tto, [group_id])

    def train(self):
        #classification_trainer.trainUntilConvergence()
        #this will take forever (possibly literally in the pathological case)

        # classification
        self.data_sets._convertToOneOfMany()

        # self.classification_trainer.trainEpochs(30)
        print("Converging...This is going to take long!")
        self.classification_trainer.trainUntilConvergence()

    def save(self, file_name="classifier.brain"):
        with open(get_path(file_name), 'wb') as file_pointer:
            pickle.dump(self.classifier_neural_net, file_pointer)

    def load(self, file_name="classifier.brain"):
        with open(get_path(file_name), 'rb') as file_pointer:
            self.classifier_neural_net = pickle.load(file_pointer)

    def accuracy(self):
        if len(self.data_sets) == 0:
            print "No data_sets found. Maybe you loaded the classifier from a file?"
            return

        # regression
        # tstresult = self.classifier_neural_net.activateOnDataset(self.data_sets)
        # print self.data_sets['target']
        # tstresult = mean_squared_error(self.data_sets['target'], tstresult)
        # print "epoch: %4d" % self.classification_trainer.totalepochs, \
        #       "trainer error: %5.2f%%" % tstresult, \
        #       "trainer accuracy: %5.2f%%" % (100-tstresult)

        # classification
        tstresult = percentError(
                        self.classification_trainer.testOnClassData(dataset=self.data_sets),
                        self.data_sets['class']
                    )

        print "epoch: %4d" % self.classification_trainer.totalepochs, \
              "trainer error: %5.2f%%" % tstresult, \
              "trainer accuracy: %5.2f%%" % (100-tstresult)

    def classify(self, image_file):
        score = self.classifier_neural_net.activate(io.twelve_tone(image_file))
        print(score)

        # regression
        # score = round(score)

        # classification
        score = max(xrange(len(score)), key=score.__getitem__)

        print(score)
        if score == 0:
            return "chick-peas"
        elif score == 1:
            return "green-peas"
        else:
            return "rice"
