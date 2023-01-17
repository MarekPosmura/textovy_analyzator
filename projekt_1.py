"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Pošmura
email: m.posmura@seznam.cz
discord: Marek P. #5306
"""
import task_template

# print(task_template.TEXTS[1])

users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
    }
line = 40*"-"

print("Welcome to the text analyzer!")
username = input("Enter your username:")
password = input("Enter your password:")

# ověřit uzivatele a heslo
if users.get(username) == password:
    print(line)
    print(f"Welcome to the app, {username}.\nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    quit()

print(line)