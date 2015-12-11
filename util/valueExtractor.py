import unicodedata

class ValueExtractor:


    @staticmethod
    def booleanValueExtractor(attributeDic):
        finalList = []
        for k in attributeDic:
            if attributeDic[k] is True:
                finalList.append(unicodedata.normalize('NFKD', k).encode('ascii', 'ignore'))
        return finalList

    @staticmethod
    def listValueExtractor(attributeList):
        finalList = []
        for val in attributeList:
            finalList.append(unicodedata.normalize('NFKD', val).encode('ascii', 'ignore'))
        return finalList
