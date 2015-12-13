import sys

from algorithm.dataSet import DataSet

ref_user_id = "kGgAARL2UmvCcTRfiscjug"

reload(sys)
sys.setdefaultencoding("utf8")
dataSet = DataSet('static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json')
dataSet.loadBusinessModels()
print dataSet.compute_user_model()


# if __name__ == "__main__":
#     main()
