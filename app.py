import sys

from datetime import datetime
from algorithm.dataSet import DataSet
from algorithm.knn import Knn
from util.MAE import getRating, MAE
from plots.bubblePlot import BubblePlot
from settings import SYS_ENCODING_UTF, JSON_FILE_PATH, JSON_FILE_NAME, PLOT_RESULTS, DISTANCE_TO_FILTER, TIME_TO_FILTER, \
    KNN_NEIGHBOURS, ENABLE_DISTANCE_FILTER, ENABLE_TIME_FILTER

reload(sys)
sys.setdefaultencoding(SYS_ENCODING_UTF)
dataSet = DataSet(JSON_FILE_PATH + JSON_FILE_NAME)
dataSet.loadRawData()
dataSet.processBusinessModels()
dataSet.sliceData()
dataSet.trainUserModel()


if ENABLE_TIME_FILTER:
    dataSet.timeFilterBusinessModel(TIME_TO_FILTER)

if ENABLE_DISTANCE_FILTER:
    dataSet.distFilterBusinessModel(DISTANCE_TO_FILTER)

knn = Knn()
knn.inputData = dataSet
predictions = knn.getNearestNeighbours(KNN_NEIGHBOURS)

for index, p in enumerate(predictions):
    print ("Name: %s\n" \
           "User Rating: %s\n" \
           "Business Rating: %s\n" \
           "Prediction Score: %s\n" \
            "Predicted Rating: %s \n" \
           "Prediction Rank: %s\n"
           % (p.name,
              p.stars,
              p.findHighestUserRating(dataSet.businessModels),
              p.predictionScore,
              getRating(p.predictionScore),
              index + 1))

print "MAE: %s" % MAE(predictions, dataSet.businessModels)

if PLOT_RESULTS:
    bp = BubblePlot()
    bp.testData = dataSet.testData
    bp.user = dataSet.userData
    bp.predictions = predictions
    bp.allBusinessModels = dataSet.businessModels
    bp.generate()









