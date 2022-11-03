import sqlite3
from sqlite3 import Error

def connect():
  conn = sqlite3.connect("database.db")
  return conn


def create_table(conn):
  try:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text NOT NULL, password text NOT NULL);")
                                  
  except Error as e:
    print(e)

def get_pass_by_name(conn, usern):
  try:
    c = conn.cursor()
    passw = c.execute("SELECT password FROM users WHERE username='" + usern + "';").fetchall()[0][0]
    return passw
  except IndexError as e:
    print("User Not Found")
      

