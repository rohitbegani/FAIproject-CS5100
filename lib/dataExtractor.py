from lib.mongoImport import db_connect, get_collection
import operator
import csv
import json
from bson import json_util

db = db_connect("yelp")
business = get_collection("business")
review = get_collection("review")

userdb = {}
reviewdb = []

for u in db.review.find():
	uid = u["user_id"]
	check = 0
	bid = u["business_id"]
	#check = db.business.find("categories":{"$in":["Restaurants"]}}).count()
	if uid in userdb: #and check > 0:
		userdb[uid] += 1
	else:
		userdb[uid] = 1

print max(userdb.iteritems(), key=operator.itemgetter(1)) #(u'kGgAARL2UmvCcTRfiscjug', 1427)

#db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'})

# this is the user with the maximum reviews.
max_review_user = max(userdb.iteritems(), key=operator.itemgetter(1))[0]

# we are finding all the reviews from this particular user.
for r in db.review.find({"user_id": max_review_user}):
	#getting the details of the business.
	cursor = db.business.find({"business_id": r["business_id"],
									  "categories": {"$in": ["Restaurants"] }})
	if cursor.count():
		business_data = cursor[0]
		business_attr = business_data["attributes"]
		#print r["business_id"]
		#print r["stars"]
		#print business_attr
		new_info = r.copy()
		new_info.update(business_data)
		reviewdb.append(new_info)

data = reviewdb

with open('../static/json/'+ max_review_user + '_reviews_business_model.json', 'w+') as outfile:
    json.dump(data, outfile, default=json_util.default)


#myfile = open('static/csv/'+ max_review_user + '_reviews_business_model.csv', 'wb')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(data)
