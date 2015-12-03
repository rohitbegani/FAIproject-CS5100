class Business(object):
    def __init__(self, name=None, business_id=None, location_lon=None, location_lat=None, stars=None, open_now=None):
        self.name = name
        self.business_id = business_id
        self.location_lon = location_lon
        self.location_lat = location_lat
        self.stars = stars
        self.open_now = open_now

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def business_id(self):
        return self.business_id

    @business_id.setter
    def business_id(self, business_id):
        self.business_id = business_id

    @property
    def location_lon(self):
        return self.location_lon

    @location_lon.setter
    def location_lon(self, location_lon):
        self.location_lon = location_lon

    @property
    def location_lat(self):
        return self.location_lat

    @location_lat.setter
    def location_lat(self, location_lat):
        self.location_lat = location_lat

    @property
    def stars(self):
        return self.stars

    @stars.setter
    def stars(self, stars):
        self.stars = stars

    @property
    def open_now(self):
        return self.open_now

    @open_now.setter
    def open_now(self, open_now):
        self.open_now = open_now
