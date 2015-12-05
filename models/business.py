class Business(object):
    def __init__(self, name=None, business_id=None, location_lon=None, location_lat=None, stars=None, open_now=None):
        self._name = name
        self._business_id = business_id
        self._location_lon = location_lon
        self._location_lat = location_lat
        self._stars = stars
        self._open_now = open_now

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

    def __str__(self):
        return "business_id: %s\n" \
               "name: %s\n" \
               "location_lat: %s\n" \
               "location_lon: %s\n" \
               "stars: %s\n" \
               "open_now: %s\n" \
               % (self.business_id,
                  self.name,
                  self.location_lat,
                  self.location_lon,
                  self.stars,
                  self.open_now)
