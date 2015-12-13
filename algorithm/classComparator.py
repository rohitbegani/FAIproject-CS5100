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
        if self.business.ambience:
            for uData in self.user.ambience:
                for bData in self.business.ambience:
                    if bData == uData[0]:
                        factor += uData[1]
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
        if self.business.good_for:
            for uData in self.user.good_for:
                for bData in self.business.good_for:
                    if bData == uData[0]:
                        factor += uData[1]
                        break
        return factor

    def parking(self):
        factor = 0.0
        if self.business.parking:
            for uData in self.user.parking:
                for bData in self.business.parking:
                    if bData == uData[0]:
                        factor += uData[1]
                        break
        return factor

    def categories(self):
        factor = 0.0
        if self.business.categories:
            for uData in self.user.categories:
                for bData in self.business.categories:
                    if bData == uData[0]:
                        factor += uData[1]
                        break
        return factor

    def dietary_restrictions(self):
        factor = 0.0
        if self.business.dietary_restrictions:
            for uData in self.user.dietary_restrictions:
                for bData in self.business.dietary_restrictions:
                    if bData == uData[0]:
                        factor += uData[1]
                        break
        return factor

    def misc_attributes(self):
        factor = 0.0
        if self.business.misc_attributes:
            for uData in self.user.misc_attributes:
                for bData in self.business.misc_attributes:
                    if bData == uData[0]:
                        factor += uData[1]
                        break
        return factor



