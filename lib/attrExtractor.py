from lib.mongoImport import db_connect, get_collection
import operator
import csv
import json
from bson import json_util

db = db_connect("yelp")
business = get_collection("business")
review = get_collection("review")

userdb = {}
attr = {}

cursor = db.business.find({"categories": {"$in": ["Restaurants"] }})
for b in cursor:
#	for a in b["attributes"]:
	attr.update(b["attributes"])

with open('../static/json/categories.json', 'w+') as outfile:
    json.dump(attr, outfile, default=json_util.default)


#myfile = open('../static/csv/categories.csv', 'w+')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(attr)
