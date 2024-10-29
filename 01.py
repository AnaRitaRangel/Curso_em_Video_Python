## Class #04

## Develop a program that asks for the user name, age and weight and prints all this information
name = input("Type your name: ")
age = input("Type your age: ")
weight = input("Type your weight in kilos: ")
print(f"{name} is {age} years old and weights {weight} kilos")

## Challenge:
# 1. Develop a program that asks for the user name and greets him/her with a personalized message
print(f"Hello, {name}! Nice to meet you!")
print(name, "is a great person!")

# 2. Ask for month, day and year of birth of the user and print a message with the formatted date
month = int(input("Type the month you were born: "))
day = int(input("Type the day you were born: "))
year = input("Type the year you were born: ")
print(name, "was born in ", month, "/", day,"/", year)

# 3. Show the sum of the user's month and day of birth
sum = month + day
print("The sum of your month and day of birth is ", sum)
