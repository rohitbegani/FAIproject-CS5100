class Hours:

    def __init__(self, sunday=None, monday=None, tuesday=None, wednesday=None, friday=None, thursday=None,
                 saturday=None):
        self._sunday = sunday
        self._monday = monday
        self._tuesday = tuesday
        self._wednesday = wednesday
        self._thursday = thursday
        self._friday = friday
        self._saturday = saturday


    @property
    def sunday(self):
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        self._sunday = sunday

    @property
    def monday(self):
        return self._monday

    @monday.setter
    def monday(self, monday):
        self._monday = monday

    @property
    def tuesday(self):
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        self._tuesday = tuesday

    @property
    def wednesday(self):
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        self._wednesday = wednesday

    @property
    def thursday(self):
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        self._thursday = thursday

    @property
    def friday(self):
        return self._friday

    @friday.setter
    def friday(self, friday):
        self._friday = friday

    @property
    def saturday(self):
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        self._saturday = saturday

    def __str__(self):
        return "[sunday: %s]" \
               "[monday: %s]" \
               "[tuesday: %s]" \
               "[wednesday: %s]" \
               "[thursday: %s]" \
               "[friday: %s]" \
               "[saturday: %s]" \
               % (self.sunday,
                  self.monday,
                  self.tuesday,
                  self.wednesday,
                  self.thursday,
                  self.friday,
                  self.saturday)


