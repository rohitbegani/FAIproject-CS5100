import pymongo

from pymongo import MongoClient
client = MongoClient()

db = client['moviedb']
movie_collection = db.movies
ratings_collection = db.ratings
tags_collection = db.tags
links_collection = db.links

def find_movie (name):
	for movie in movie_collection.find({ "title" : {'$regex': "/^%s" % (name) }}):
		print movie

find_movie("Innocence")


# for movie in movie_collection.find():
# 	print movie