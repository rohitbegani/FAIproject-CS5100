import json

from models.business import Business

with open('/home/bhanu/Documents/MSCS/AI/proj/FAIproject-CS5100'
          '/static/json/kGgAARL2UmvCcTRfiscjug_reviews_business_model.json') as data_file:
    data = json.load(data_file)

businessList =[]
set = set()
for i, obj in enumerate(data):
    business = Business()
    business.id = obj["attributes"]
    music = business.id["Ambience"]
    for m in music:
        set.add(m)
    for s in set:
        print(s)
    # print  music
    # businessList.append(business)
