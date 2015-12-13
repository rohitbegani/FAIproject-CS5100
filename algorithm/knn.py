import collections

import operator

from algorithm.classComaprator import ClassComparator


class Knn(object):
    def __init__(self, inputData=None):
        self.inputData = inputData

    def getNearestNeighbours(self, k):
        """
         This method retursn the 'k' nearest neighbours for the data
         :param k: the no neighbours
         """
        nDict = {}
        neighbours = []
        for dataRow in self.inputData.testData:
            nDict[dataRow] = self.getSimilarityFactor(dataRow)
            sortedList = sorted(nDict.items(), key=operator.itemgetter(1), reverse=True)
        for sortedValue in sortedList[:k]:
            neighbours.append(sortedValue[0])
            print(sortedValue[0].name)
            print(sortedValue[1])
        return neighbours

    def getSimilarityFactor(self, dataRow):
        """
        This method returns the similarity factor of the most given dataRow and the user.
        :param dataRow:
        """
        cc = ClassComparator()
        cc.user = self.inputData.userData
        cc.business = dataRow
        similarityFactor = 0.0
        similarityFactor += cc.wifi() \
                            + cc.alcohol()
        return similarityFactor
