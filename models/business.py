import unicodedata

from util.valueExtractor import ValueExtractor


class Business(object):
    def __init__(self, name=None, business_id=None, location_lon=None, location_lat=None, stars=None, open_now=None,
                 wifi=None, alcohol=None, noise_level=None, music=None, attire=None, ambience=None, price_range=None,
                 good_for=None, parking=None, categories=None):

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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        self._business_id = business_id

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
        self._wifi = wifi

    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, alcohol):
        self._alcohol = alcohol

    @property
    def noise_level(self):
        return self._noise_level

    @noise_level.setter
    def noise_level(self, noise_level):
        self._noise_level = noise_level

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
        self._attire = attire

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
        self._parking = ValueExtractor.booleanValueExtractor(parking)

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = ValueExtractor.listValueExtractor(categories)

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
                  self.categories)


