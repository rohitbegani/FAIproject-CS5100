import json
import os
from datetime import timedelta, datetime

import math

from models.user import User
from settings import REF_USER_ID, REF_USER_NAME
from util.jsonToObject import Decode
from random import shuffle


class DataSet(object):
    def __init__(self, jsonFile=None):
        # Store Default Values for KNN
        self.jsonFile = jsonFile
        self.testData = None
        self.trainingData = None
        self.userData = None
        self._rawData = None
        self._businessModels = None

    def loadRawData(self):
        complete_jsonFilePath = os.path.join(os.path.abspath(os.curdir), self.jsonFile)
        with open(complete_jsonFilePath) as data_file:
            self._rawData = json.load(data_file)

    def sliceData(self):
        # Shuffle the Business Model List
        # shuffle(self._businessModels)
        test_cutoff = int(math.floor(len(self._businessModels) / 3))
        self.testData = self._businessModels[0:test_cutoff]
        self.trainingData = self._businessModels[test_cutoff:]

    def processBusinessModels(self):
        jsonDecoder = Decode()
        jsonDecoder.data = self._rawData
        businessModels = jsonDecoder.getBusiness()
        self._businessModels = businessModels

    def trainUserModel(self):
        user = User(REF_USER_ID, REF_USER_NAME)
        for td in self.trainingData:
            user.update_user(td)
        user.normalize()
        self.userData = user

    def timeFilterBusinessModel(self):
        newData = []
        today = datetime.today()
        currentTime = timedelta(hours=today.hour, minutes=today.minute)
        for d in self.testData:
            days = [d.hours.monday, d.hours.tuesday, d.hours.wednesday, d.hours.thursday,
                    d.hours.friday, d.hours.saturday, d.hours.sunday]
            openingHours = days[today.weekday()]
            if openingHours is not None:
                openingHours = openingHours.split("-")
                open = openingHours[0].split(":")
                openTime = timedelta(hours=int(open[0]), minutes=int(open[1]))
                close = openingHours[1].split(":")
                closeTime = timedelta(hours=int(close[0]), minutes=int(close[1]))
                if openTime <= currentTime < closeTime:
                    newData.append(d)
            else:
                newData.append(d)
        self.testData = newData
