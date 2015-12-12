import sys
from util.jsonToObject import Decode


class Knn(object):
    def __init__(self, businessModels=[], jsonFile=None):
        # Store Default Values for KNN
        print("Inside KNN Init")
        self._jsonFile = jsonFile
        self._businessModels = businessModels

    def load_business_models(self):
        jsonDecoder = Decode()
        jsonDecoder.jsonFilePath = self.jsonFile

        self.businessModels = jsonDecoder.get_business()
        print("Indie KNN load_business_models")
        for b in self.businessModels:
            print(b)
