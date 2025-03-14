# Exercise 22 – Text Analyzer
#Create a program that reads a person's full name and displays:
# •	The name in all uppercase and lowercase letters.
name = input("Write your full name and hit <enter>: ")
print(f"Your name in uppercase letters: {name.upper()}") # ANA RITA MOREIRA RANGEL
print(f"Your name in lowercase letters: {name.lower()}")  # ana rita moreira rangel

# •	The total number of letters (excluding spaces).
nospacename = name.replace(" ", "")
print(f"The total lenght of your name includding spaces is: {len(name)}")  # 23
print(f"The total lenght of your name without spaces is: {len(nospacename)}")  #20

# •	The number of letters in the first name.
separate_name = name.split()  # Makes a list with the words
first_name = separate_name[0]  # Gets the first element of the list
print(f"Your first name is: {first_name}")
print(f"{first_name} has {len(first_name)} letters")

