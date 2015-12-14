import unicodedata

from models.hours import Hours
from util.valueExtractor import ValueExtractor


class Business(object):
    def __init__(self, name=None, business_id=None, location_lon=None, location_lat=None, stars=None, open_now=None,
                 wifi=None, alcohol=None, noise_level=None, music=None, attire=None, ambience=None, price_range=None,
                 good_for=None, parking=None, categories=None, dietary_restrictions=None, misc_attributes=None,
                 hours=None, userRating=None, predictionScore=None):

        self._name = name
        self._business_id = business_id
        self._location_lon = location_lon
        self._location_lat = location_lat
        self._stars = stars
        self._open_now = open_now
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
        self._hours = hours
        self._userRating = userRating
        self._predictionScore = predictionScore

    @property
    def predictionScore(self):
        return self._predictionScore

    @predictionScore.setter
    def predictionScore(self, predictionScore):
        self._predictionScore = predictionScore


    @property
    def userRating(self):
        return self._userRating

    @userRating.setter
    def userRating(self, userRating):
        self._userRating = userRating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = ValueExtractor.stringValueExtractor(name)

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        self._business_id = ValueExtractor.stringValueExtractor(business_id)

    @property
    def location_lon(self):
        return self._location_lon

    @location_lon.setter
    def location_lon(self, location_lon):
        self._location_lon = location_lon

    @property
    def location_lat(self):
        return self._location_lat

    @location_lat.setter
    def location_lat(self, location_lat):
        self._location_lat = location_lat

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, stars):
        self._stars = stars

    @property
    def open_now(self):
        return self._open_now

    @open_now.setter
    def open_now(self, open_now):
        self._open_now = open_now

    @property
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, wifi):
        self._wifi = ValueExtractor.stringValueExtractor(wifi)

    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, alcohol):
        self._alcohol = ValueExtractor.stringValueExtractor(alcohol)

    @property
    def noise_level(self):
        return self._noise_level

    @noise_level.setter
    def noise_level(self, noise_level):
        self._noise_level = ValueExtractor.stringValueExtractor(noise_level)

    @property
    def music(self):
        return self._music

    @music.setter
    def music(self, music):
        self._music = ValueExtractor.booleanDictValueExtractor(music)

    @property
    def attire(self):
        return self._attire

    @attire.setter
    def attire(self, attire):
        self._attire = ValueExtractor.stringValueExtractor(attire)

    @property
    def ambience(self):
        return self._ambience

    @ambience.setter
    def ambience(self, ambience):
        self._ambience = ValueExtractor.booleanDictValueExtractor(ambience)

    @property
    def price_range(self):
        return self._price_range

    @price_range.setter
    def price_range(self, price_range):
        self._price_range = price_range

    @property
    def good_for(self):
        return self._good_for

    @good_for.setter
    def good_for(self, good_for):
        goodForList = []
        if self.good_for is not None:
            goodForList.extend(self.good_for)
        for k in good_for:
            if good_for[k] is True:
                if isinstance(k, unicode):
                    goodForList.append(unicodedata.normalize('NFKD', k).encode('ascii', 'ignore'))
                else:
                    goodForList.append(k)
        self._good_for = goodForList

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, parking):
        self._parking = ValueExtractor.booleanDictValueExtractor(parking)

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
        self._dietary_restrictions = ValueExtractor.booleanDictValueExtractor(dietary_restrictions)

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

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        hoursObject = Hours()
        if "Sunday" in hours.keys():
            day = hours["Sunday"]
            hoursObject.sunday = day["open"] + "-" + day["close"]
        if "Monday" in hours.keys():
            day = hours["Monday"]
            hoursObject.monday = day["open"] + "-" + day["close"]
        if "Tuesday" in hours.keys():
            day = hours["Tuesday"]
            hoursObject.tuesday = day["open"] + "-" + day["close"]
        if "Wednesday" in hours.keys():
            day = hours["Wednesday"]
            hoursObject.wednesday = day["open"] + "-" + day["close"]
        if "Thursday" in hours.keys():
            day = hours["Thursday"]
            hoursObject.thursday = day["open"] + "-" + day["close"]
        if "Friday" in hours.keys():
            day = hours["Friday"]
            hoursObject.friday = day["open"] + "-" + day["close"]
        if "Saturday" in hours.keys():
            day = hours["Saturday"]
            hoursObject.saturday = day["open"] + "-" + day["close"]
        self._hours = hoursObject

    def __str__(self):
        return "business_id: %s\n" \
               "name: %s\n" \
               "location_lat: %s\n" \
               "location_lon: %s\n" \
               "stars: %s\n" \
               "open_now: %s\n" \
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
               "hours: %s\n" \
               "userRating: %s\n" \
               % (self.business_id,
                  self.name,
                  self.location_lat,
                  self.location_lon,
                  self.stars,
                  self.open_now,
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
                  self.misc_attributes,
                  self.hours,
                  self.userRating)
