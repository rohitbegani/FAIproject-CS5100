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

            if "business_id" in obj.keys():
                business.business_id = obj["business_id"]
            if "name" in obj.keys():
                business.name = obj["name"]
            if "latitude" in obj.keys():
                business.location_lat = obj["latitude"]
            if "longitude" in obj.keys():
                business.location_lon = obj["longitude"]
            if "stars" in obj.keys():
                business.stars = obj["stars"]
            if "open" in obj.keys():
                business.open_now = obj["open"]
            if "categories" in obj.keys():
                business.categories = obj["categories"]

            businessList.append(self.processBusinessAttributes(business, obj))

        return businessList

    def processBusinessAttributes(self, business, obj):
        attributes = obj["attributes"]
        if "Wi-Fi" in attributes.keys():
            business.wifi = attributes["Wi-Fi"]
        if "Alcohol" in attributes.keys():
            business.alcohol = attributes["Alcohol"]
        if "Noise Level" in attributes.keys():
            business.noise_level = attributes["Noise Level"]
        if "Music" in attributes.keys():
            business.music = attributes["Music"]
        if "Attire" in attributes.keys():
            business.attire = attributes["Attire"]
        if "Ambience" in attributes.keys():
            business.ambience = attributes["Ambience"]
        if "Price Range" in attributes.keys():
            business.price_range = attributes["Price Range"]
        if "Good For" in attributes.keys():
            business.good_for = attributes["Good For"]
        if "Good For Kids" in attributes.keys() and attributes["Good For Kids"] is True:
            business.good_for = {"kids": True}
        if "Good For Groups" in attributes.keys() and attributes["Good For Groups"] is True:
            business.good_for = {"groups": True}
        if "Good For Dancing" in attributes.keys() and attributes["Good For Dancing"] is True:
            business.good_for = {"dancing": True}
        if "Parking" in attributes.keys():
            business.parking = attributes["Parking"]
        return business
