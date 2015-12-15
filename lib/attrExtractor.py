from lib.mongoImport import db_connect, get_collection

db = db_connect("yelp")
business = get_collection("business")
review = get_collection("review")

userdb = {}

def get_attr_value(key):
	attr = []
	for r in db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'}):
		#getting the details of the business.
		cursor = db.business.find({"business_id": r["business_id"],
										  "categories": {"$in": ["Restaurants"] }})
		if cursor.count():
			attrs = cursor[0]["attributes"]
			#print attrs
			for k in attrs:
				if k == key:
					if attrs[k] not in attr:
						attr.append(attrs[k])
	return attr


def get_sub_attr(sub_attr):
	attr = []
	for r in db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'}):
		#getting the details of the business.
		cursor = db.business.find({"business_id": r["business_id"],
										  "categories": {"$in": ["Restaurants"] }})
		if cursor.count() and cursor[0]["attributes"].has_key(sub_attr):
			attrs = cursor[0]["attributes"][sub_attr]
			#print attrs
			for k in attrs:
				if k not in attr:
					attr.append(k)
		else:
			# print "skipped"
			# print cursor[0]["attributes"]
			continue

	return attr

def get_sub_attr_value(sub_attr, key):
	attr = []
	for r in db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'}):
		#getting the details of the business.
		cursor = db.business.find({"business_id": r["business_id"],
										  "categories": {"$in": ["Restaurants"] }})
		if cursor.count() and cursor[0]["attributes"].has_key(sub_attr):
			attrs = cursor[0]["attributes"][sub_attr]
			#print attrs
			for k in attrs.keys():
				if k == key:
					if attrs[k] not in attr:
						attr.append(attrs[k])

	return attr

def get_all_attr():
	attr = []
	for r in db.review.find({"user_id": 'kGgAARL2UmvCcTRfiscjug'}):
		#getting the details of the business.
		cursor = db.business.find({"business_id": r["business_id"],
										  "categories": {"$in": ["Restaurants"] }})
		if cursor.count():
			attrs = cursor[0]["attributes"]
			#print attrs
			for k in attrs.keys():
				if k not in attr:
						attr.append(k)
	return attr


data = get_sub_attr("Dietary Restrictions")
print data
#data = get_attr_value("Ages Allowed")
#print data


#with open('../static/json/attr_data_dump.json', 'w+') as outfile:
#    json.dump(data.append(data2).append(data3), outfile, default=json_util.default)


#myfile = open('../static/csv/categories.csv', 'w+')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(attr)
