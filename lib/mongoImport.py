from pymongo import MongoClient

client = MongoClient()

db = client['moviedb']
movie_collection = db.movies
ratings_collection = db.ratings
tags_collection = db.tags
links_collection = db.links


def db_connect(db):
    client = MongoClient()
    db = client[db]
    return db


def get_collection(name):
    return db.name


def find_movie(name):
    for movie in movie_collection.find({"title": {'$regex': "/^%s" % (name)}}):
        print movie


def test():
    for movie in movie_collection.find():
        for r in ratings_collection.find({"movieId": movie["movieId"]}):
            print movie, r
            break
        for t in tags_collection.find({"movieId": movie["movieId"]}):
            print t
            break
        for l in links_collection.find({"movieId": movie["movieId"]}):
            print l
            break
        break

# print ratings_collection.find({"userId": 295}).count()



# for rating in ratings_collection.find():
#	print rating["movieId"]
