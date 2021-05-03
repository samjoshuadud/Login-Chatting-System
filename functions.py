from client import *
from server import *
import sqlite3

conn = sqlite3.connect('registration.db')
c = conn.cursor()


class SignUp:
    def __init__(self, username, password, dname):
        self.username = username
        self.password = password
        self.dname = dname


    def signu(self):
        c.execute(f'''INSERT INTO info (username, password, name) VALUES ('{self.username}', '{self.password}', '{self.dname}'); ''')
        conn.commit()


class Signin:
    def __init__(self, username, dname):
        self.username = username
        self.display = dname
        print(f"You are now login! {self.display}\n")
        while 1:
            print(f"\n[a] Enter the Chat room\n[b] Enter/Change Display name\n")
            choice = input("ENTER YOUR CHOICE: ")
            if choice == 'a':
                try:
                    run(self.display)
                except:
                    clientr(self.display)
                break
            elif choice == 'b':
                ch = input("Display Name: ")
                c.execute(f"UPDATE info SET name ='{ch}' where username = '{self.username}';").fetchone()
                conn.commit()
                continue
