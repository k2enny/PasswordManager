from utils import endecrypt, sqlutil
import hashlib

#Inizio MySql
conn = sqlutil.connect()
sqlutil.create_table_users(conn)
sqlutil.create_table_passw(conn)
c = conn.cursor()

#Organizzaziond Utenti
user = None
upass = None
print("Scegli un'opzione: \n1) Nuovo utente \n2) Utente già esistente")
newUser = input("Opzione: ")
if newUser == '1':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  if sqlutil.check_user(conn, usern) == False:
    quit("Utente già esistente")
  c.execute("INSERT INTO users ('username', 'password') VALUES ('" + usern +
            "', '" + hashedPw.hexdigest() + "');")
  user = usern
  upass = passw

if newUser == '2':
  usern = input('username: ')
  passw = input('password: ')
  hashedPw = hashlib.sha512(passw.encode('utf-8'))
  rightPass = sqlutil.get_pass_by_name(conn, usern)

  if rightPass == hashedPw.hexdigest():
    user = usern
    upass = passw
  else:
    quit("Wrong Password")

#Password Manager
print("Scegli un'opzione: \n1) Nuova password \n2) Get password")
newPassw = input("Opzione: ")
if newPassw == '1':
  name = input("Password Name: ")
  passw = input("Password: ")
  enpassw = endecrypt.encrypt(upass.encode('utf-8'), passw.encode('utf-8'))
  c.execute("INSERT INTO password ('name', 'password', 'user') VALUES ('" + name + "', '" + enpassw + "', '" + user + "');")

if newPassw == '2':
  list = 0
  nlist = c.execute("SELECT name FROM password WHERE user='" + user +
                    "'").fetchall()
  for n in nlist:
    list += 1
    print(str(list) + ") " + str(n[0]))
  passn = int(input("Password Number: "))
  plist = c.execute("SELECT password FROM password WHERE user='" + user + "'").fetchall()
  print(endecrypt.decrypt(upass.encode('utf-8'), str(plist[passn - 1])).decode('utf-8'))

conn.commit()
conn.close()