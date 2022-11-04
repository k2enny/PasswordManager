import sqlite3
from sqlite3 import Error

def connect():
  conn = sqlite3.connect("database.db")
  return conn


def create_table_users(conn):
  try:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text NOT NULL, password text NOT NULL);")
                                  
  except Error as e:
    print(e)

def create_table_passw(conn):
  try:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS password (name text NOT NULL, password text NOT NULL, user text NOT NULL);")
                                  
  except Error as e:
    print(e)

def get_pass_by_name(conn, usern):
  try:
    c = conn.cursor()
    passw = c.execute("SELECT password FROM users WHERE username='" + usern + "';").fetchall()[0][0]
    return passw
  except IndexError as e:
    quit("User Not Found")

def check_user(conn, usern):
  try:
    c = conn.cursor()
    user = c.execute("SELECT username FROM users WHERE username='" + usern + "';").fetchall()[0][0]
    quit("Utente già esistente")
  except IndexError as er:
    pass