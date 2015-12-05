import json
import os

from models.business import Business


class Decode:
    def __init__(self, jsonFilePath=None):
        self._jsonFilePath = jsonFilePath

    def get_business(self):
        os.chdir("..")
        complete_jsonFilePath = os.path.join(os.path.abspath(os.curdir), self.jsonFilePath)
        with open(complete_jsonFilePath) as data_file:
            data = json.load(data_file)

        businessList = []
        for i, obj in enumerate(data):
            business = Business()

            business.business_id = obj["business_id"]
            business.name = obj["name"]
            business.location_lat = obj["latitude"]
            business.location_lon = obj["longitude"]
            business.stars = obj["stars"]
            business.open_now = obj["open"]

            businessList.append(business)
        return businessList
