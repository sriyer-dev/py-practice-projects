import datetime
import uuid
from todo.db.db import DB


class Item:
    def __init__(self, title, target_date, description=None,
                 create_date=None):
        self.title = title
        self.description = description
        self.create_date = datetime.datetime.utcnow() if create_date is None else create_date
        self.target_date = datetime.datetime.strptime(target_date, '%d/%m/%Y')
        self.status = 'Open'
        self.complete_date = None
        self._id = uuid.uuid4().hex
        DB()

    def json(self):
        return {
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date,
            'create_date': self.create_date,
            'status': self.status,
            'complete_date': self.complete_date,
            'user': 'xyz',
            '_id': self._id,
        }

    def save(self):
        DB.insert('items', self.json())
        return {
            'status': 'record inserted'
        }

    @classmethod
    def find_one(cls, query):
        return DB.find_one('items', query)

    @classmethod
    def find_all(cls):
        items = DB.find('items', {'user': 'xyz'})
        return {
            'items': [item for item in items]
        }

    @staticmethod
    def update(data):
        # if type(data['target_date']) == 'str':
        #     data['target_date'] = datetime.datetime.strptime(data['target_date'], '%d/%m/%Y')
        return DB.update('items', data['_id'], data)

