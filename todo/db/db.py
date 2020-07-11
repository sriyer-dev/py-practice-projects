import datetime

import pymongo


class DB:
    URI= 'mongodb://127.0.0.1:27017'
    db = None

    @staticmethod
    def initialize():
        DB.client = pymongo.MongoClient(DB.URI)
        DB.db = DB.client['todolist']

    @staticmethod
    def insert(coll, data):
        DB.db[coll].insert(data)

    @staticmethod
    def find_one(coll, query):
        return DB.db[coll].find_one(query)

    @staticmethod
    def find(coll, query):
        return DB.db[coll].find(query)

    @staticmethod
    def update(coll, _id, data):
        record = {}
        for k, v in data.items():
            record[k] = v
        result = DB.db[coll].update_one({'_id': _id}, {'$set': record})
        return {
            'status': 'successfully updated ' + str(result.modified_count) + ' record(s)'
        }

