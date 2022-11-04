#Importazione delle librerie:
from utils import endecrypt, sqlutil
import hashlib

#Inizio MySql:
conn = sqlutil.connect()
sqlutil.create_table_users(conn)
sqlutil.create_table_passw(conn)
c = conn.cursor()

#Organizzazione Utenti:
#Inizializzazione della sessione
user = None
upass = None
print("Scegli un'opzione: \n1) Nuovo utente \n2) Utente già esistente")
newUser = input("Opzione: ")
#Creazione nuovo utente
if newUser == '1':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  #Controllo utente già esistente
  if sqlutil.check_user(conn, usern) == False:
    quit("Utente già esistente")
  sqlutil.add_user(conn, usern, hashedPw.hexdigest())
  user = usern
  upass = passw
#Utente già esistente
if newUser == '2':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  rightPass = sqlutil.get_pass_by_name(conn, usern)
  #Controllo password
  if rightPass == hashedPw.hexdigest():
    user = usern
    upass = passw
  else:
    quit("Password sbagliata")

#Password Manager
print("Scegli un'opzione: \n1) Nuova password \n2) Ottieni password")
newPassw = input("Opzione: ")
#Nuova password
if newPassw == '1':
  name = input("Password Name: ")
  passw = input("Password: ")
  enpassw = endecrypt.encrypt(upass.encode('utf-8'), passw.encode('utf-8'))
  sqlutil.add_password(conn, name, enpassw, user)
#Ottieni lista password
if newPassw == '2':
  list = 0
  nlist = c.execute("SELECT name FROM password WHERE user='" + user + "'").fetchall()
  for n in nlist:
    list += 1
    print(str(list) + ") " + str(n[0]))
  #Controllo lista password non vuota
  if list == 0:
    quit("Nessuna password salvata")
  passn = int(input("Password Number: "))
  plist = c.execute("SELECT password FROM password WHERE user='" + user + "'").fetchall()
  print(endecrypt.decrypt(upass.encode('utf-8'), str(plist[passn - 1])).decode('utf-8'))

#Chiusura connessioni MySQL
conn.commit()
conn.close()

#☆☆☆☆☆☆☆☆☆☆☆☆
#
#if (WhoMade.is(k2enny)) {
#  System.out.println("k2ennyyyy");
#}
#
#☆☆☆☆☆☆☆☆☆☆☆☆