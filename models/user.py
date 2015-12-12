import unicodedata

from models.hours import Hours
from util.valueExtractor import ValueExtractor


class User(object):

    def __init__(self, name=None, user_id=None, stars=None, location_lat=None, location_lon=None,
                 wifi={}, alcohol={}, noise_level={}, music={}, attire={}, ambience={}, price_range={},
                 good_for=None, parking={}, categories={}, dietary_restrictions={}, misc_attributes=None):
        self._name = self.name(name)
        self._user_id = self.user_id(user_id)
        self._stars = self.stars(stars)
        self._location_lat = self.location_lat(location_lat)
        self._location_lon = self.location_lon(location_lon)
        self._wifi = self.wifi(wifi)
        self._alcohol = self.alcohol(alcohol)
        self._noise_level = self.noise_level(noise_level)
        self._music = self.music(music)
        self._attire = self.attire(attire)
        self._ambience = self.ambience(ambience)
        self._price_range = self.price_range(price_range)
        self._good_for = self.good_for(good_for)
        self._parking = self.parking(parking)
        self._categories = self.categories(categories)
        self._dietary_restrictions = self.dietary_restrictions(dietary_restrictions)
        self._misc_attributes = self.misc_attributes(misc_attributes)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = "John Doe"

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def location_lat(self):
        return self._location_lat

    @location_lat.setter
    def location_lat(self):
    	self._location_lat = 36.11470649999999

    @property
    def location_lon(self):
        return self._location_lon

    @location_lon.setter
    def location_lon(self):
    	self._location_lon = -115.17284840000002

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, stars):
        self._stars = stars

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
        for m in music:
            self._music = self.update_feature_weight(self._music, m)

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
        for a in ambience:
            self._ambience = self.update_feature_weight(self._music, a)

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
        for i in good_for:
            self._good_for = self.update_feature_weight(self._good_for, i)

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, parking):
       for p in parking:
            self._parking = self.update_feature_weight(self._parking, p)

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        for c in categories:
            self._categories = self.update_feature_weight(self._categories, c)

    @property
    def dietary_restrictions(self):
        return self._dietary_restrictions

    @dietary_restrictions.setter
    def dietary_restrictions(self, dietary_restrictions):
       for d in dietary_restrictions:
            self._dietary_restrictions = self.update_feature_weight(self._dietary_restrictions, d)


    @property
    def misc_attributes(self):
        return self._misc_attributes

    @misc_attributes.setter
    def misc_attributes(self, misc_attributes):
       for m in misc_attributes:
            self._misc_attributes = self.update_feature_weight(self._misc_attributes, m)


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

    def set_features(self, stars=None, location_lat=None, location_lon=None, wifi={}, alcohol={},
                     noise_level={}, music={}, attire={}, ambience={}, price_range={},
                 good_for=None, parking={}, categories={}, dietary_restrictions={}, misc_attributes=None):
        self._stars = self.stars(stars)
        self._location_lat = self.location_lat(location_lat)
        self._location_lon = self.location_lon(location_lon)
        self._wifi = self.wifi(wifi)
        self._alcohol = self.alcohol(alcohol)
        self._noise_level = self.noise_level(noise_level)
        self._music = self.music(music)
        self._attire = self.attire(attire)
        self._ambience = self.ambience(ambience)
        self._price_range = self.price_range(price_range)
        self._good_for = self.good_for(good_for)
        self._parking = self.parking(parking)
        self._categories = self.categories(categories)
        self._dietary_restrictions = self.dietary_restrictions(dietary_restrictions)
        self._misc_attributes = self.misc_attributes(misc_attributes)

    def compute_feature_weight(self, weight, value, rating):
        return weight + value * rating

    def update_feature_weight (self, feature, value):
        temp = feature
        if value in temp.keys():
            (v, w) = temp[value]
            w = self.compute_feature_weight(w, value, self.stars)
            temp[value] = (v, w)
        else:
            temp[value] = (value, 0)
        return temp

    def normalize_feature_weight(self, feature):
        """
        Iterates through all the weight vectors and normalizes its values to 1.
        """
        n = sum(feature.values())
        for k in feature.keys():
            feature[k] /= n
        return feature

    def normalize(self):
        self._wifi = self.normalize_feature_weight(self._wifi)
        self._alcohol = self.normalize_feature_weight(self._alcohol)
        self._noise_level = self.normalize_feature_weight(self._noise_level)
        self._music = self.normalize_feature_weight(self._music)
        self._attire = self.normalize_feature_weight(self._attire)
        self._ambience = self.normalize_feature_weight(self._ambience)
        self._price_range = self.normalize_feature_weight(self._price_range)
        self._good_for = self.normalize_feature_weight(self._good_for)
        self._parking = self.normalize_feature_weight(self._parking)
        self._categories = self.normalize_feature_weight(self._categories)
        self._dietary_restrictions = self.normalize_feature_weight(self._dietary_restrictions)
        self._misc_attributes = self.normalize_feature_weight(self._misc_attributes)






