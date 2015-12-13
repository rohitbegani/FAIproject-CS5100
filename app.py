import sys

from algorithm.dataSet import DataSet

reload(sys)
sys.setdefaultencoding("utf8")
dataSet = DataSet('static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json')
dataSet.loadRawData()
dataSet.processBusinessModels()
dataSet.sliceData()
dataSet.trainUserModel()
print(len(dataSet.trainingData))
print(len(dataSet.testData))
print(dataSet.userData)