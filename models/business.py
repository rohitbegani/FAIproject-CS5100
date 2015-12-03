class Business(object):
    def __init__(self, name=None, business_id=None):
        self.name = name
        self.business_id = business_id

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
