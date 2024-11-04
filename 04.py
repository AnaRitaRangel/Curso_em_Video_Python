## CLASS 08 ##
print("==== Square Root ====")
from math import sqrt #Import just the sqrt method from the math library
n = float(input("Type a number: "))
square_rt = sqrt(n)
print(f"The square root of {n} is {square_rt:.2f}")


import math #Import the whole library
n2 = float(input("Type a number: "))
square_root = math.sqrt(n2)
print(f"The square root of {n2} is {square_root:.2f}")

## Generate a random interger
print("==== Generate a Random number ====")
import random
begin_number = input("Type the lower number: ")
last_number = input("Type the higher number: ")
random_number = random.randint(begin_number,last_number)
print(random_number)

## Emoji
print("==== Message with an emoji ====")
import emoji
print(emoji.emojize("Hello, World! :earth_americas:", language="alias"))


## 16. Develop a program that given a float number, displays just the interger part of it
print("==== Get the interger part of a real number (floating-point) ====")
import math
num = float(input("Type a float number: "))
inter = math.trunc(num)
print(f"The interger part of {num} is {inter}")

## If I treat the input as a string I can use 'split'
interger, decimal = num.split('.')
print(f"The interger part of {num} is {interger}")


## No need to import math, just converting a float into an interger
num = float(input("Type a float number: "))
inte = int(num)
print(f"The interger part of {num} is {inte}")


## 17. Write a program that reads the length of the opposite side and the adjacent side of a right triangle. Calculate and display the length of the hypotenuse.
print("==== Calculate the hypothenuse ====")
import math
opposite_side = float(input("Type the opposite side of the right triangle: "))
adjacent_side = float(input("Type the adjacent side of the right triangle: "))
hypotenuse = (opposite_side ** 2 + adjacent_side ** 2) **0.5
print(f"The value for the hypotenhuse of a right triangle with opposite side of {opposite_side} and adjacent side of {adjacent_side} is {hypotenuse:.2f}")

##17 option
import math
opposite_side = float(input("Type the opposite side of the right triangle: "))
adjacent_side = float(input("Type the adjacent side of the right triangle: "))
hypotenuse = math.hypot(opposite_side, adjacent_side)
print(f"The value for the hypotenhuse of a right triangle with opposite side of {opposite_side} and adjacent side of {adjacent_side} is {hypotenuse:.2f}")

## 18. Write a program that reads any angle and displays the sine, cosine, and tangent values of that angle
print("==== Sine, Cosine and Tangent ====")
import math
angle = float(input("Type a value for the angle: "))
#You have to transform the angle to radians
angle_radians = math.radians(angle)
sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)
print(f"The values for {angle}º angle are:\nSine: {sine:.3f}\nCosine: {cosine:.3f}\nTangent: {tangent:.3f}")

## 19. A teacher wants to randomly select one of their four students to erase the board. Write a program to help them by reading the students' names and displaying the name of the chosen student on the screen.
print("==== Pick someone randomly ====")
import random
# Get input from the user and convert it to a list by splitting on commas
names = input("Type a list of the names separated by commas (e.g., a, b, c): ").split(',')
choice = random.choice(names)
print(f"The chosen name is: {choice}")

## 20. A teacher wants to randomize the presentation order of the students' assignments. Write a program that reads the names of four students and displays the randomized order.
print("==== Pick the order for presenting the assignment ====")
import random
name1 = input("Type the first name: ")
name2 = input("Type the second name: ")
name3 = input("Type the third name: ")
name4 = input("Type the fourth name: ")
lista = [name1, name2, name3, name4]
random.shuffle(lista)
print(f"The order for the presentation is: {lista})")

## 21: Write a program in Python that opens and plays the audio from an MP3 file.
import pygame
import time

# Initialize Pygame
pygame.mixer.init()

# Load the MP3 file
mp3_file = '/Users/anaritamoreirarangel/Documents/guanabara/serenity-waves.mp3'  # Full path

try:
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    # Keep the program running while the music is playing
    while pygame.mixer.music.get_busy(): 
        time.sleep(1)

except pygame.error as e:
    print(f"An error occurred: {e}")
