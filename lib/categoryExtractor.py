from lib.mongoImport import db_connect, get_collection
import operator
import csv
import json
from bson import json_util

db = db_connect("yelp")
business = get_collection("business")
review = get_collection("review")

userdb = {}
cat = []

cursor = db.business.find({"categories": {"$in": ["Restaurants"] }})
for i in cursor:
	cat += i["categories"]


#with open('../static/json/categories.json', 'w+') as outfile:
#    json.dump(cat, outfile, default=json_util.default)


myfile = open('../static/csv/categories.csv', 'w+')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(cat)
