class ClassComparator:
    def __init__(self, user=None, business=None):
        self.user = user
        self.business = business

    def wifi(self):
        factor = 0.0
        for data in self.user.wifi:
            if self.business.wifi == data[0]:
                factor = data[1]
                break
        return factor

    def alcohol(self):
        factor = 0.0
        for data in self.user.alcohol:
            if self.business.alcohol == data[0]:
                factor = data[1]
                break
        return factor
