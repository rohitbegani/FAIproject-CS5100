import sys

from algorithm.dataSet import DataSet
from settings import SYS_ENCODING_UTF, JSON_FILE_PATH, JSON_FILE_NAME

reload(sys)
sys.setdefaultencoding(SYS_ENCODING_UTF)
dataSet = DataSet(JSON_FILE_PATH + JSON_FILE_NAME)
dataSet.loadRawData()
dataSet.processBusinessModels()
dataSet.sliceData()
dataSet.trainUserModel()
print(len(dataSet.trainingData))
print(len(dataSet.testData))
print(dataSet.userData)
