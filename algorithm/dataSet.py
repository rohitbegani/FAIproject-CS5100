import json
import os
import math
from datetime import timedelta

from math import sin, cos, radians, atan2, sqrt
from models.user import User
from models.business import Business
from settings import REF_USER_ID, REF_USER_NAME
from util.jsonToObject import Decode
from random import shuffle


class DataSet(object):
    def __init__(self, jsonFile=None):
        # Store Default Values for KNN
        self.jsonFile = jsonFile
        self.testData = None
        self.trainingData = None
        self.businessModels = None
        self.userData = User()
        self._rawData = None

    def loadRawData(self):
        complete_jsonFilePath = os.path.join(os.path.abspath(os.curdir), self.jsonFile)
        with open(complete_jsonFilePath) as data_file:
            self._rawData = json.load(data_file)

    def sliceData(self):
        # Shuffle the Business Model List
        # shuffle(self._businessModels)
        test_cutoff = int(math.floor(len(self.businessModels) / 3))
        self.testData = self.filterDuplicates(self.businessModels[0:test_cutoff])
        self.trainingData = self.businessModels[test_cutoff:]

    def processBusinessModels(self):
        jsonDecoder = Decode()
        jsonDecoder.data = self._rawData
        businessModels = jsonDecoder.getBusiness()
        self.businessModels = businessModels

    def trainUserModel(self):
        user = User(REF_USER_ID, REF_USER_NAME)
        for td in self.trainingData:
            user.update_user(td)
        user.normalize()
        self.userData = user

    def timeFilterBusinessModel(self, timeNow):
        newData = []
        today = timeNow
        currentTime = timedelta(hours=today.hour, minutes=today.minute)
        for d in self.testData:
            days = [d.hours.monday, d.hours.tuesday, d.hours.wednesday, d.hours.thursday,
                    d.hours.friday, d.hours.saturday, d.hours.sunday]
            openingHours = days[today.weekday()]
            if openingHours is not None and openingHours != "00:00-00:00":
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

    ## Using the Haversine Formula
    ## http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

    def distFilterBusinessModel(self, rad=1):
        '''
        This function implements the Haversine formula to calculate the
        distance from the users current location to the location of the
        business
        :param rad: 1
        :return: appends business within a mile
        '''
        newData = []
        latUser = self.userData.location_lat
        lonUser = self.userData.location_lon
        for b in self.testData:
            latBus = b.location_lat
            lonBus = b.location_lon
            lon1, lat1, lon2, lat2 = map(radians, [lonBus, latBus, lonUser, latUser])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            radius = 6371
            distance = radius * c
            if distance < rad:
                newData.append(b)
        self.testData = newData

    def filterDuplicates(self, data):
        list = []
        for d in data:
            f = 0
            for l in list:
                if l.name == d.name:
                    f=1
                    break
            if f == 0:
                list.append(d)
        return list
