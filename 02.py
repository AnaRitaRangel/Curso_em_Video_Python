## Class # 06

#4. Develop a program that reads an input and shows which type it is and all the possible information about it
print('What can be told about the input')
value = input("Type something: ")

# My solution:
if not value:
    print("You haven´t typed anything")
elif value.isalpha():
    print("What you typed contains only letters")
elif value.isnumeric():
    print("What you typed is a number")
elif value.isalnum():
    print("What you typed contains letters and numbers")
else:
     print("What you typed contains special characters or other symbols")
## To verify if what was typed before was written with upper or lower case letters I can put two more conditions: It can´t be put in the first part of the code because it would be excludent, meaning, it would only classify what comes first, leaving the latter conditions not judged
if value.isupper():
    print("You used only upper case letters")
elif value.islower():
    print("You used only lower case letters")
elif value.istitle(): # Only first letter capital
    print("You capitalized the input")


# Teacher's solution:
print("")
print("")
print("")
print("## THIS IS THE TEACHER'S SOLUTION ##")
print("The input is blank: ", value.isspace())
print("The input contains only letters: ", value.isalpha())
print("The input contains only numbers: ", value.isnumeric())
print("The input contains only letters and/or numbers: ", value.isalnum())

