from tinydb import TinyDB, Query


class TinyDBCookbook(object):
    def __init__(self, db_path):
        self._db = TinyDB(db_path)

    def upsert(self, recipe):
        query = Query()
        self._db.upsert(recipe, query.name == recipe['name'])

    def retrieve(self, recipe_name):
        query = Query()
        return self._db.get(query.name == recipe_name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.close()
