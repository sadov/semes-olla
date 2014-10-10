#!/bin/env python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient

#client = MongoClient('mongodb://admin:IhKg4RdY9Lcy@5436735c4382ec447e00026d-olla.rhcloud.com:40661/')
client = MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])

db = client.semes
ce=db.CannibEllie

dictionary = ce.find_one({'lang':'English'})['dict']
