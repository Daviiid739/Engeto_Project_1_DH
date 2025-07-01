"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Horák
email: daviiid739@gmail.com
"""

import sys

#   Variables
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
line = "-" * 40
texts_count = len(TEXTS)
users = {
        "bob": "123", 
        "ann": "pass123", 
        "mike": "password123", 
        "liz": "pass123"
}


#   Check if the user is registered.
username = input("username: ")
password = input("password: ")

if username in users.keys() and password == users.get(username):
    print(line)
    print(f"Welcome to the app, {username}\nWe have {texts_count} texts to be analyzed.")
    print(line)

else:
    print("unregistered user, terminating the program..")
    sys.exit()    


#   Select texts
text_number = input(f"Enter a number btw. 1 and {texts_count} to select: ")
print(line)

if text_number.isdecimal():
    text_number = int(text_number)
    if text_number > texts_count or text_number <= 0:
        print(f"Number {text_number} is not in range between 1 and {texts_count}.", "Terminating the program..", sep="\n")
        sys.exit()

else:
    print(f"Incorrect input. An integer btw. 1 and {texts_count} must be entered.", "Terminating the program..", sep="\n")
    sys.exit()

selected_text = TEXTS[text_number-1]


#   Loop Variables
title_count = 0
upper_count = 0
lower_count = 0
number_count = 0
number_list = []
words_len = {}

#   Spliting the text to single words
raw_words = selected_text.split()

for raw_word in raw_words:
    word = raw_word.strip(".,;:!?()[]{}'\"")

#   Number of words starting with a capital letter
    if word.istitle():
        title_count += 1

#   Number of words written in capital letters
    if word.isupper():
        upper_count += 1
    
#   Number of words written in lowercase letters
    if word.islower():    
        lower_count += 1

#   Number of numbers (not digits)
    if word.isnumeric():
        number_count += 1
        number_list.append(int(word))   

#   Frequency of word lengths
    if len(word) not in words_len:
        words_len[len(word)] = 1
    else:
        words_len[len(word)] += 1

#   Counting the words
text_len = len(raw_words)

#   Sum of all numbers (not digits) in the text
number_sum = sum(number_list)

#   Printing the results
print(f"There are {text_len} words in the selected text.")
print(f"There are {title_count} titlecase words.")
print(f"There are {upper_count} uppercase words.")
print(f"There are {lower_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers: {number_sum}")


#   Chart header
print(line)
print(f"{"LEN":>3}|{"OCCURENCES".center(20)}|{"NR."}")
print(line)

#   Simple bar chart
sorted_words_len = sorted(words_len)

for key in sorted_words_len:
    value = words_len.get(key)
    star_count = "*" * value
    print(f"{key:>3}|{star_count:<20}|{value}")
