import sys

from algorithm.dataSet import DataSet

ref_user_id = "kGgAARL2UmvCcTRfiscjug"

def main():
    reload(sys)
    sys.setdefaultencoding("utf8")
    dataSet = DataSet('static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json')
    dataSet.loadBusinessModels()


if __name__ == "__main__":
    main()
