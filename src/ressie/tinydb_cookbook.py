from tinydb import TinyDB, Query
from contextlib import contextmanager


class TinyDBCookbook(object):
    def __init__(self, db_path):
        self._db = TinyDB(db_path)

    def upsert(self, recipe):
        query = Query()
        self._db.upsert(recipe.to_dict(), query.name == recipe.name)

    def retrieve(self, recipe_name):
        query = Query()
        return self._db.get(query.name == recipe_name)

    @contextmanager
    def open(self):
        yield self
        self._db.close()
