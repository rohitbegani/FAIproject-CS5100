import unicodedata

from models.hours import Hours
from util.valueExtractor import ValueExtractor


class User(object):

    def __init__(self, name=None, user_id=None, stars=None, location_lat=None, location_lon=None,
                 wifi={}, alcohol={}, noise_level={}, music={}, attire={}, ambience={}, price_range={},
                 good_for=None, parking={}, categories={}, dietary_restrictions={}, misc_attributes=None):
        self.name = name
        self.user_id = user_id
        self._stars = stars
        self.location_lat = location_lat
        self.location_lon = location_lon
        self._wifi = wifi
        self._alcohol = alcohol
        self._noise_level = noise_level
        self._music = music
        self._attire = attire
        self._ambience = ambience
        self._price_range = price_range
        self._good_for = good_for
        self._parking = parking
        self._categories = categories
        self._dietary_restrictions = dietary_restrictions
        self._misc_attributes = misc_attributes

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self):
        self.name = "John Doe"

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, user_id):
        self.user_id = user_id

    @property
    def location_lat(self):
        return self.location_lat

    @location_lat.setter
    def location_lat(self):
    	self.location_lat = 36.11470649999999

    @property
    def location_lon(self):
        return self.location_lon

    @location_lon.setter
    def location_lon(self):
    	self.location_lon = -115.17284840000002

    @property
    def stars(self):
        return self.stars

    @stars.setter
    def stars(self, stars):
        self.stars = stars

    @property
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, wifi):
        self._wifi = self.update_feature_weight(self._wifi, wifi)

    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, alcohol):
        self._alcohol = self.update_feature_weight (self._alcohol, alcohol)

    @property
    def noise_level(self):
        return self._noise_level

    @noise_level.setter
    def noise_level(self, noise_level):
        self._noise_level = self.update_feature_weight(self._noise_level, noise_level)

    @property
    def music(self):
        return self._music

    @music.setter
    def music(self, music):
        self._music = ValueExtractor.booleanValueExtractor(music)

    @property
    def attire(self):
        return self._attire

    @attire.setter
    def attire(self, attire):
        self._attire = self.update_feature_weight(self._attire, attire)

    @property
    def ambience(self):
        return self._ambience

    @ambience.setter
    def ambience(self, ambience):
        self._ambience = ValueExtractor.booleanValueExtractor(ambience)

    @property
    def price_range(self):
        return self._price_range

    @price_range.setter
    def price_range(self, price_range):
        self._price_range = self.update_feature_weight(self._price_range, price_range)

    @property
    def good_for(self):
        return self._good_for

    @good_for.setter
    def good_for(self, good_for):
        pass

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, parking):
        self._parking = ValueExtractor.booleanValueExtractor(parking)

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = ValueExtractor.listValueExtractor(categories)

    @property
    def dietary_restrictions(self):
        return self._dietary_restrictions

    @dietary_restrictions.setter
    def dietary_restrictions(self, dietary_restrictions):
        self._dietary_restrictions = ValueExtractor.booleanValueExtractor(dietary_restrictions)

    @property
    def misc_attributes(self):
        return self._misc_attributes

    @misc_attributes.setter
    def misc_attributes(self, misc_attributes):
        miscAttrList = []
        if self.misc_attributes is not None:
            miscAttrList.extend(self.misc_attributes)
        miscAttrList.append(misc_attributes)
        self._misc_attributes = miscAttrList

    def __str__(self):
        return "user_id: %s\n" \
               "name: %s\n" \
               "location_lat: %s\n" \
               "location_lon: %s\n" \
               "stars: %s\n" \
               "wifi: %s\n" \
               "alcohol: %s\n" \
               "noise_level: %s\n" \
               "music: %s\n" \
               "attire: %s\n" \
               "ambience: %s\n" \
               "price_range: %s\n" \
               "good_for: %s\n" \
               "parking: %s\n" \
               "categories: %s\n" \
               "dietary_restrictions: %s\n" \
               "misc_attributes: %s\n" \
               % (self.user_id,
                  self.name,
                  self.location_lat,
                  self.location_lon,
                  self.stars,
                  self.wifi,
                  self.alcohol,
                  self.noise_level,
                  self.music,
                  self.attire,
                  self.ambience,
                  self.price_range,
                  self.good_for,
                  self.parking,
                  self.categories,
                  self.dietary_restrictions,
                  self.misc_attributes)

    def compute_feature_weight(self, feature, value, rating):
        pass


    def update_feature_weight (self, feature, value):
        temp = feature
        if value in temp.keys():
            (v, w) = temp[value]
            w = self.compute_feature_weight(w, value, self.stars)
            temp[value] = (v, w)
        else:
            temp[value] = (value, 0)
        return temp

    def normalize_weights (self):
        pass

    def value_setter(self, *args, **kwargs): # real signature unknown
            """ Descriptor to change the setter on a property. """
            for arg in args:
                if arg == True:
                    return 1
                elif arg == False:
                    return 0
                else:
                    return 0
            pass