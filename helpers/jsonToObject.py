import json

from models.business import Business
from models.user import User


def user_object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'User':
        return User(obj['name'], obj['id'])
    return obj


def business_object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Business':
        return Business(obj['name'], obj['id'])
    return obj


def review_object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Review':
        return Business(obj['id'], obj['business_id'])
    return obj
