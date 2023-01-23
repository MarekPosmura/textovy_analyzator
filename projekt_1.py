"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Pošmura
email: m.posmura@seznam.cz
discord: Marek P. #5306
"""
import task_template

users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
    }
line = 40*"-"

print("Welcome to the text analyzer!")

# vyžádat si jméno a heslo a ověřit údaje
username = input("Enter your username: ")
password = input("Enter your password: ")

if users.get(username) == password:
    print(line)
    print(f"Welcome to the app, {username}.\nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    quit()
print(line)

# výběr textu
selected_num = input("Enter a number btw. 1 and 3 to select: ")
if selected_num < "1" or selected_num > "3":
    print("Wrong number, terminating the program...")
    quit()
print(line)

# úprava textu
selected_text = task_template.TEXTS[int(selected_num)-1]
edited_text = list()

# počet slov
for word in selected_text.split():
    edited_text.append(word.strip(",.-"))
print(f"There are {len(edited_text)} words in the selected text.")

# počet slov začínajících velkým písmenem
titlecase_words = dict()
for word in edited_text:
    if str(word).istitle(): 
        titlecase_words[word] = 1
print(f"There are {len(titlecase_words)} titlecase words.")

# počet slov psaných velkými písmeny
uppercase_words = dict()
for word in edited_text:
    if str(word).isupper() and str(word).isalpha(): 
        uppercase_words[word] = 1
print(f"There are {len(uppercase_words)} uppercase words.")

# počet slov psaných malými písmeny
lowercase_words = list()
for word in edited_text:
    if word.islower():
        lowercase_words.append(word)
print(f"There are {len(lowercase_words)} lowercase words.")

# počet čísel (ne cifer)
numeric_string = list()
for word in edited_text:
    if word.isnumeric():
        numeric_string.append(word)
print(f"There are {len(numeric_string)} numeric strings.")

# sumu všech čísel (ne cifer) v textu
sum_numbers = 0
for word in edited_text:
    if word.isdigit() == True:
            number = int(word)
            sum_numbers += number
print(f"The sum of all the numbers {sum_numbers}.")
print(line)

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu
tab = print(("LEN|".rjust(4)), "OCCURENCES".rjust(10), "|NR.".rjust(5))
print(line)
length = {}
for word in edited_text:
    if len(word) not in length:
        length[len(word)] = 1
    else:
        length[len(word)] += 1 

for key, value in sorted(length.items()):
    print(f"{str(key).rjust(3)}|{'*'*(int(value))} |{value}")
print(line)