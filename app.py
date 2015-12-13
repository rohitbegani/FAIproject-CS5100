
import sys

from datetime import datetime
from algorithm.dataSet import DataSet
from algorithm.knn import Knn
from settings import SYS_ENCODING_UTF, JSON_FILE_PATH, JSON_FILE_NAME

reload(sys)
sys.setdefaultencoding(SYS_ENCODING_UTF)
dataSet = DataSet(JSON_FILE_PATH + JSON_FILE_NAME)
dataSet.loadRawData()
dataSet.processBusinessModels()
dataSet.sliceData()
print(len(dataSet.testData))
dataSet.trainUserModel()
dataSet.timeFilterBusinessModel(datetime.today())
dataSet.distFilterBusinessModel(5)
#for d in dataSet.trainingData:
#     print(d)
print(len(dataSet.trainingData))
print(len(dataSet.testData))
# print(dataSet.userData)

knn = Knn()
knn.inputData = dataSet
prediction = knn.getNearestNeighbours(5)