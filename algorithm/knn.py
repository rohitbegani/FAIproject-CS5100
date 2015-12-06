import sys

import knn as knn

from helpers.jsonToObject import Decode


class Knn(object):
    def __init__(self, businessModels=[], jsonFile=None):
        # Store Default Values for KNN
        print("Inside KNN Init")
        self._jsonFile = jsonFile
        self._businessModels = businessModels

    def load_business_models(self):

        jsonDecoder = Decode()
        jsonDecoder.jsonFilePath = self.jsonFile

        self.businessModels = jsonDecoder.get_business()
        print("Indie KNN load_business_models")
        for b in self.businessModels:
            print(b)


def main():
    reload(sys);
    sys.setdefaultencoding("utf8")
    knn = Knn()
    knn.jsonFile = 'static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json'
    knn.load_business_models()


if __name__ == "__main__":
    main()
