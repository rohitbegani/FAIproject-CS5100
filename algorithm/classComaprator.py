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

    def noise_level(self):
        factor = 0.0
        for data in self.user.noise_level:
            if self.business.noise_level == data[0]:
                factor = data[1]
                break
        return factor

    def noise_level(self):
        factor = 0.0
        for data in self.user.noise_level:
            if self.business.noise_level == data[0]:
                factor = data[1]
                break
        return factor

    def music(self):
        factor = 0.0
        for data in self.user.music:
            if self.business.music == data[0]:
                factor = data[1]
                break
        return factor

    def attire(self):
        factor = 0.0
        for data in self.user.attire:
            if self.business.attire == data[0]:
                factor = data[1]
                break
        return factor

    def ambience(self):
        factor = 0.0
        for data in self.user.ambience:
            if self.business.ambience == data[0]:
                factor = data[1]
                break
        return factor

    def price_range(self):
        factor = 0.0
        for data in self.user.price_range:
            if self.business.price_range == data[0]:
                factor = data[1]
                break
        return factor

    def good_for(self):
        factor = 0.0
        for data in self.user.good_for:
            if self.business.good_for == data[0]:
                factor = data[1]
                break
        return factor

    def parking(self):
        factor = 0.0
        for data in self.user.parking:
            if self.business.parking == data[0]:
                factor = data[1]
                break
        return factor

    def categories(self):
        factor = 0.0
        for data in self.user.categories:
            if self.business.categories == data[0]:
                factor = data[1]
                break
        return factor

    def dietary_restrictions(self):
        factor = 0.0
        for data in self.user.dietary_restrictions:
            if self.business.dietary_restrictions == data[0]:
                factor = data[1]
                break
        return factor

    def misc_attributes(self):
        factor = 0.0
        for data in self.user.misc_attributes:
            if self.business.misc_attributes == data[0]:
                factor = data[1]
                break
        return factor


