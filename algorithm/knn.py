import operator

from algorithm.classComparator import ClassComparator


class Knn(object):
    def __init__(self, inputData=None):
        self.inputData = inputData

    def getNearestNeighbours(self, k):
        """
         This method returns the 'k' nearest neighbours for the data
         :param k: the no neighbours
         """
        nDict = {}
        neighbours = []
        for dataRow in self.inputData.testData:
            nDict[dataRow] = self.getSimilarityFactor(dataRow)
        sortedList = sorted(nDict.items(), key=operator.itemgetter(1), reverse=True)
        for sortedValue in sortedList[:k]:
            sortedValue[0].predictionScore = sortedValue[1]
            neighbours.append(sortedValue[0])
        return neighbours

    def getSimilarityFactor(self, dataRow):
        """
        This method returns the similarity factor of the most given dataRow and the user.
        :param dataRow: It the each row of Business in the test data
        """

        cc = ClassComparator()
        cc.user = self.inputData.userData
        cc.business = dataRow
        similarityFactor = 0.0

        factor = [cc.wifi(),
        cc.alcohol(),
        cc.noise_level(),
        cc.music(),
        cc.attire(),
        cc.ambience(),
        cc.price_range(),
        cc.good_for(),
        cc.parking(),
        cc.categories(),
        cc.dietary_restrictions(),
        cc.misc_attributes()]
        total = 0
        count = 0
        # for f in factor:
        #     if f != 0.0:
        #         count += 1
        #         total += f
        # return total/count

        for f in factor:
            total += f
        return total




        # similarityFactor += cc.wifi() \
        #                     + cc.alcohol() \
        #                     + cc.noise_level() \
        #                     + cc.music() \
        #                     + cc.attire() \
        #                     + cc.ambience() \
        #                     + cc.price_range() \
        #                     + cc.good_for() \
        #                     + cc.parking() \
        #                     + cc.categories() \
        #                     + cc.dietary_restrictions() \
        #                     + cc.misc_attributes()
        # return similarityFactor
