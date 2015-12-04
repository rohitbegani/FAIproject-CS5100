class User(object):

    def __init__(self, name=None, id=None):
        self.name = name
        self.user_id = user_id
        self.stars = stars
        self.location_lat = location_lat
        self,location_lon = location_lon


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
    def stars(self):
        return self.stars

    @stars.setter
    def stars(self, stars):
        self.stars = stars

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