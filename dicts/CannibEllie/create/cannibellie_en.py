#!/bin/env python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient

#client = MongoClient('mongodb://admin:IhKg4RdY9Lcy@5436735c4382ec447e00026d-olla.rhcloud.com:40661/')
client = MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])

db = client.semes
ce=db.CannibEllie

ce.insert(
{'lang':'English', 'dict': [
{"item": "You're being vulgar."},
{"item": "Ho-ho ", "descr": "expresses irony, surprise, delight, loathing, joy, contempt and satisfaction, according to the circumstances"},
{"item": "Great!"},
{"item": "Dismal ", "descr": "applied to everything-for example: \"dismal Pete has arrived\", \"dismal weather\", or a \"dismal cat\""},
{"item": "Gloom."},
{"item": "Ghastly ", "descr": "for example: when meeting a close female acquaintance, \"a ghastly meeting\""},
{"item": "Kid ", "descr": "applied to all male acquaintances, regardless of age or social position"},
{"item": "Don't tell me how to live!"},
{"item": "Like a babe ", "descr": "\"I whacked him like a babe\" when playing cards, or \"I brought him down like a babe,\" evidently when talking to a legal tenant"},
{"item": "Ter-r-rific!"},
{"item": "Fat and good-looking ", "descr": "used to describe both animate and inanimate objects"},
{"item": "Let's go by horse-cab ", "descr": "said to her husband"},
{"item": "Let's go by taxi ", "descr": "said to male acquaintances"},
{"item": "You're all white at the back! ", "descr": "joke"},
{"item": "Just imagine!"},
{"item": "Ula ", "descr": "added to a name to denote affection-for example: Mishula, Zinula"},
{"item": "Oho! ", "descr": "irony, surprise, delight, loathing, joy, contempt and satisfaction"}
]})
