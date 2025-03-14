## CLASS 09 ##
# Operations with strings in Python. The main operations we will cover are string slicing, analysis with len(), count(), find(), transformations with replace(), upper(), lower(), capitalize(), title(), strip(), and joining with join()

phrase = "Curso em Video Python"
print(phrase[9:13])   # output takes 9, 10, 11 and 12 = Vide 
print(phrase[9:21:2])    # output takes 9, 11, 13, 15, 17 and 19(jumps every2) = VdoPto
print(phrase[:5])    # output takes 0, 1, 2, 3 and 4 (Beggining up to 4)= Curso
print(phrase[15:])    # output takes 15, 16, 17, 18, 19 and 20 = Python
print(phrase[9::3])    # output takes 9, 12, 15 and 18 = VePh
print(len(phrase))         # shows the lenghth of the string (# of characters) = 21
print(phrase.count("o"))         # counts how many (o) you have on that string = 3
print(phrase.count("o", 0,13))      # counts how many (o) you have on that interval = 1
print(phrase.find("deo"))      # shows which position "deo" starts = 11
print(phrase.find("Android"))      # since you can't find it, it returns -1
print("Curso" in phrase)     # Is there "Curso" in phrase? Returns True of False = True

print(phrase.replace("Curso", "Android"))       # Replace
print(len(phrase))         # It doesn't change the original lenghth of the string = 21
print(len(phrase.replace("Curso", "Android")))       # Now it changes = 23
separate = phrase.split()  # Separates the string and makes a list = [Curso, em, Video, Python]. ** You need to call the split() method on phrase by adding parentheses () after split to execute the function
print(separate)        
print(' '.join(separate))       #Will join the list with a blank space between the words = Curso em Video Python
print(''.join(separate))       #Will join the list with no space between the words = CursoemVideoPython

