import sqlite3 as lite
import sys

def user_menu():
    print("Login menu")
    print()
    print("1. Login")
    print("2. Create Account")
    print("0. Exit Program")

def get_user_menu_choice():
    accepted = False
while not accepted:
    choice = int(input("Please select an option: "))
    if 0 <= choice <= 2:
        accepted = True
    else:
        print("Pleae enter a valid value:")
    return choice

def query(sql,data):
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def insert_data(values):
    sql = "insert into Product (name,password) values(?,?)"
query(sql,values)

def main():
    finished = False
while not finished:
    user_menu()
    choice = get_user_menu_choice()
    if choice == 1:
        # Get login details from user
        user = input('User: ')
        password = getpass.getpass('Password: ')
        # Connect to database
        db = sqlite3.connect('DATABASE') 
        c = db.cursor()
        # Execute sql statement and grab all records where the "usuario" and
        # "senha" are the same as "user" and "password"
        c.execute('SELECT * FROM Product', (user, password))
        # If nothing was found then c.fetchall() would be an empty list, 

        if c.fetchall():
         print('Welcome')
        else:
            print('Login failed')
    elif choice == 2:
        name = input("Please enter name of name ")
        password = input("Please enter the passsword {0}: ".format(name))
        insert_data((name,password))
    elif choice == 0:
        finished = True
    else:
        finished = True

if __name__ == "__main__":
    DATABASE = "userlogins.db"
main()