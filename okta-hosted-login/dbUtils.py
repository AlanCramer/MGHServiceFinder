#db
import sqlite3
from flask import g

DATABASE = 'testDb.db'

def connect_db():
    return sqlite3.connect(DATABASE)

# @app.before_request
def before_request():
    g.db = connect_db()

# @app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(DATABASE)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

