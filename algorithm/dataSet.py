import json
import os
import sys
from util.jsonToObject import Decode
from numpy.random import permutation


class DataSet(object):
    def __init__(self, jsonFile=None):
        # Store Default Values for KNN
        print("Inside KNN Init")
        self.jsonFile = jsonFile
        self._rawData = self.loadData()
        # self._testData = testData
        # self._trainData = trainData
        self._businessModels = self.loadBusinessModels()

    def loadData(self):
        print(self.jsonFile)
        complete_jsonFilePath = os.path.join(os.path.abspath(os.curdir), self.jsonFile)
        with open(complete_jsonFilePath) as data_file:
            return json.load(data_file)

    def shuffleData(self):
        # Shuffle the indexes of the loaded data
        random = permutation(self._rawData.index)

    def loadBusinessModels(self):
        jsonDecoder = Decode()
        jsonDecoder.data = self._rawData
        businessModels = jsonDecoder.get_business()
        print("Indie KNN load_business_models")
        for b in businessModels:
            print(b)
        return businessModels
