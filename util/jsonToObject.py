import json
import os

from models.business import Business


class Decode:
    def __init__(self, jsonFilePath=None, data=None):
        self._jsonFilePath = jsonFilePath
        self._data = data

    def getBusiness(self):
        businessList = []
        for i, obj in enumerate(self.data):
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
            if "hours" in obj.keys():
                business.hours = obj["hours"]
            if "userRating" in obj.keys():
                business.userRating = obj["userRating"]
            if "text" in obj.keys():
                business.userReview = obj["text"]
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
        if "Dietary Restrictions" in attributes.keys():
            business.dietary_restrictions = attributes["Dietary Restrictions"]
        if "Delivery" in attributes.keys() and attributes["Delivery"] is True:
            business.misc_attributes = "delivery"
        if "Coat Check" in attributes.keys() and attributes["Coat Check"] is True:
            business.misc_attributes = "coat_check"
        if "Smoking" in attributes.keys() and attributes["Smoking"] is True:
            business.misc_attributes = "smoking"
        if "Accepts Credit Cards" in attributes.keys() and attributes["Accepts Credit Cards"] is True:
            business.misc_attributes = "accepts_credit_cards"
        if "Take-out" in attributes.keys() and attributes["Take-out"] is True:
            business.misc_attributes = "take_out"
        if "Happy Hour" in attributes.keys() and attributes["Happy Hour"] is True:
            business.misc_attributes = "happy_hour"
        if "Wheelchair Accessible" in attributes.keys() and attributes["Wheelchair Accessible"] is True:
            business.misc_attributes = "wheelchair_accessible"
        if "Outdoor Seating" in attributes.keys() and attributes["Outdoor Seating"] is True:
            business.misc_attributes = "outdoor_seating"
        if "Takes Reservations" in attributes.keys() and attributes["Takes Reservations"] is True:
            business.misc_attributes = "takes_reservations"
        if "Waiter Service" in attributes.keys() and attributes["Waiter Service"] is True:
            business.misc_attributes = "waiter_service"
        if "Has TV" in attributes.keys() and attributes["Has TV"] is True:
            business.misc_attributes = "has_tv"
        if "BYOB" in attributes.keys() and attributes["BYOB"] is True:
            business.misc_attributes = "byob"
        if "Dogs Allowed" in attributes.keys() and attributes["Dogs Allowed"] is True:
            business.misc_attributes = "dogs_allowed"
        if "Drive-thru" in attributes.keys() and attributes["Drive-thru"] is True:
            business.misc_attributes = "drive_through"
        if "Open 24 hours" in attributes.keys() and attributes["Open 24 hours"] is True:
            business.misc_attributes = "open_24_hours"

        return business
