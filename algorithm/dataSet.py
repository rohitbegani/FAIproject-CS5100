import json
import os
import sys
from util.jsonToObject import Decode
from models.user import User
# import random
# from numpy.random import permutation

ref_user_id = "kGgAARL2UmvCcTRfiscjug"


class DataSet(object):
    def __init__(self, jsonFile=None):
        # Store Default Values for KNN
        print("Inside KNN Init")
        self.jsonFile = jsonFile
        self._user = User(ref_user_id, "Bob")
        self._rawData = self.loadData()
        # self._testData = testData
        # self._trainData = trainData
        self._businessModels = self.loadBusinessModels()


    def loadData(self):
        print(self.jsonFile)
        complete_jsonFilePath = os.path.join(os.path.abspath(os.curdir), self.jsonFile)
        with open(complete_jsonFilePath) as data_file:
            return json.load(data_file)

    # def shuffleData(self):
        # Shuffle the indexes of the loaded data
        # random = permutation(self._rawData.index)

    def loadBusinessModels(self):
        jsonDecoder = Decode()
        jsonDecoder.data = self._rawData
        businessModels = jsonDecoder.get_business()
        print("Indie KNN load_business_models")
        #for b in businessModels:
        #    print(b)
        return businessModels

    def update_user(self, business):
        b = business
        self._user.add_features(b.stars, b.location_lat, b.location_lon, b.wifi, b.alcohol, b.noise_level, b.music,
                              b.attire, b.ambience, b.price_range, b.good_for,
                              b.parking, b.categories, b.dietary_restrictions, b.misc_attributes)


    def compute_user_model(self):
        for b in self._businessModels:
            self.update_user(b)
            print self._user
        self._user.normalize()
        print self._user