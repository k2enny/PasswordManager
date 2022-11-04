#Importazione librerie
import sqlite3
from sqlite3 import Error

#Creazione connessione con database
def connect():
  conn = sqlite3.connect("database.db")
  return conn

#Crea tabella degli utenti
def create_table_users(conn):
  try:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text NOT NULL, password text NOT NULL);")
                                  
  except Error as e:
    print(e)

#Crea tabella delle password
def create_table_passw(conn):
  try:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS password (name text NOT NULL, password text NOT NULL, user text NOT NULL);")
                                  
  except Error as e:
    print(e)

#Ottieni password di un utente
def get_pass_by_name(conn, usern):
  try:
    c = conn.cursor()
    passw = c.execute("SELECT password FROM users WHERE username='" + usern + "';").fetchall()[0][0]
    return passw
  except IndexError as e:
    quit("Utente non trovato")

#Controllo utente già esistente
def check_user(conn, usern):
  try:
    c = conn.cursor()
    user = c.execute("SELECT username FROM users WHERE username='" + usern + "';").fetchall()[0][0]
    quit("Utente già esistente")
  except IndexError as er:
    pass

#Aggiungi password abbinata ad utente
def add_password(conn, name, enpassw, user):
  c = conn.cursor()
  c.execute("INSERT INTO password ('name', 'password', 'user') VALUES ('" + name + "', '" + enpassw + "', '" + user + "');")
  conn.commit()

#Aggiungi utente
def add_user(conn, usern, hashedPw):
  c = conn.cursor()
  c.execute("INSERT INTO users ('username', 'password') VALUES ('" + usern + "', '" + hashedPw + "');")
  conn.commit()
