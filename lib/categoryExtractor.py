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

# for u in db.review.find():
# 	uid = u["user_id"]
# 	check = 0
# 	bid = u["business_id"]
# 	#check = db.business.find("categories":{"$in":["Restaurants"]}}).count()
# 	if uid in userdb: #and check > 0:
# 		userdb[uid] += 1
# 	else:
# 		userdb[uid] = 1
#
# print max(userdb.iteritems(), key=operator.itemgetter(1)) #(u'kGgAARL2UmvCcTRfiscjug', 1427)
#
# # this is the user with the maximum reviews.
# max_review_user = max(userdb.iteritems(), key=operator.itemgetter(1))[0]
#

for r in db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'}):
	#getting the details of the business.
	cursor = db.business.find({"business_id": r["business_id"],
									  "categories": {"$in": ["Restaurants"] }})
	if cursor.count():
		for c in cursor[0]["categories"]:
			if c not in cat:
				cat.append(c)




with open('../static/json/categories.json', 'w+') as outfile:
    json.dump(cat, outfile, default=json_util.default)


#myfile = open('../static/csv/categories.csv', 'w+')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(cat)
