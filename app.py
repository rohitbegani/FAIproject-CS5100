from algorithm.knn import Knn

ref_user_id = "kGgAARL2UmvCcTRfiscjug"

knn = Knn()
knn.jsonFile = 'static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json'
knn.load_business_models()