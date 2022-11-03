from utils import endecrypt, sqlutil
import hashlib

#Inizio MySql
conn = sqlutil.connect()
sqlutil.create_table(conn)
c = conn.cursor()

#Organizzaziond Utenti
print("Scegli un'opzione: \n1) Nuovo utente \n2) Utente già esistente")
newUser = input("Opzione: ")
if newUser == '1':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  c.execute("INSERT INTO users ('username', 'password') VALUES ('" + usern + "', '" + hashedPw.hexdigest() + "');")

if newUser == '2':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  rightPass = sqlutil.get_pass_by_name(conn, usern)
  
  if rightPass == hashedPw.hexdigest():
    print('Success')
  
  
print(c.execute("SELECT * FROM users").fetchall())

conn.commit()

en = endecrypt.encrypt(b"passw", b"hi")
print(en)
de = endecrypt.decrypt(b"passw", en)
print(de)
