from functions import *
import stdiomask
from os import system

conn = sqlite3.connect('registration.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS info (username     TEXT    NOT NULL, password      TEXT    NOT NULL, name  TEXT      NOT NULL);''')
conn.commit()

def su():
    while 1:
        system('cls||clear')
        username = input("Username: ")
        if c.execute(f'''SELECT username FROM info where username='{username}' ''').fetchone():
            print("Existing Username, Try Again!")
            input("Press Enter")
            continue
        password = stdiomask.getpass("Password: ")
        if len(password) < 4:
            print("\nPassword must be greater than 4! ")
            input("\nPress Enter")
            continue
        while 1:
            displayname = input("Enter a Display name: ")
            if c.execute(f"SELECT name FROM info where name='{displayname}'").fetchone():
                print("Existing Display name. Please enter again!")
                continue
            else:
                break

        s = SignUp(username, password, displayname)
        s.signu()
        break

def si():
    while 1:
        system('cls||clear')
        username = input("Username: ")
        password = stdiomask.getpass("Password: ")
        if c.execute(f"SELECT username FROM info where username='{username}' ").fetchone() and c.execute(f"SELECT password FROM info where password='{password}' ").fetchone():
            name = ''
            for i in c.execute(f"SELECT name FROM info where username='{username}';").fetchone():
                name = i
                break
            Signin(username, name)
            break
        else:
            print("Wrong Username or Password")
            input("Press Enter to try again")


while 1:
    print("[a] Sign In\n[b] Sign Up\n[c] Exit")
    choice = input("\n Enter your Choice: ")
    if choice == 'a':
        si()
    elif choice == 'b':
        su()
        system('cls||clear')
        print("Done!\n")
        input("Press Enter if Satisfied..")
    elif choice == 'c':
        break
    else:
        print("Wrong Shit")
        continue


