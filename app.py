import sys

from datetime import datetime
from algorithm.dataSet import DataSet
from algorithm.knn import Knn
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

def getRating(score):
    if score == 0:
        return 0
    elif score in range(0, 1):
        return 0.5
    elif score in range(1,2):
        return 1
    elif score in range(2,3):
        return 1.5
    elif score in range(3,4):
        return 2
    elif score in range(4,5):
        return 2.5
    elif score in range(5,6):
        return 3
    elif score in range(6,7):
        return 3.5
    elif score in range(7,8):
        return 4
    elif score in range(8,9):
        return 4.5
    elif score in range(9,10):
        return 5
    else:
        return None


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

if PLOT_RESULTS:
    bp = BubblePlot()
    bp.testData = dataSet.testData
    bp.user = dataSet.userData
    bp.predictions = predictions
    bp.allBusinessModels = dataSet.businessModels
    bp.generate()









