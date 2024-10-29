## Class # 7
## 5. Develop a program that writes the antecessor and successor of a number
print("=== Antecessor and sucessor of a number ===")
n = int(input("Give me a number: "))
print(f"The antecessor of {n} is {n - 1}, and its sucessor is {n + 1}")

## 6. Develop a program that gives the double, triple and the square root of a number
print('')
print("=== double, triple and the square root ===")
print(f"The double of {n} is {n * 2}, and its triple is {n * 3}, while its square root is {n ** 1/2:.2f}")

## 7. Develop a program that reads two test scores of a student and returns the average between them
print('')
print("=== Average ===")
g1 = float(input("Type your first score: "))
g2 = float(input("Type your second score: "))
m = (g1 + g2) / 2
print(f"Your average is {m}")

## 8. Develop a program that reads a number in meters and converts it to centimeters and milimeters
print('')
print("=== Convert meters to cm and mm ===")
meter = float(input("Type a measure in meters: "))
cm = meter * 100 
mm = meter * 1000
print(f"{meter}m is equivalent to {cm}cm")
print(f"{meter}m is equivalent to {mm}mm")

## 9. Develop a program that reads an interger number and shows its multiplication table
print('')
print("=== Multiplication table ===")
n = int(input("Type an interger number: "))
print(f"{n} X 1 = {n * 1}")
print(f"{n} X 2 = {n * 2}")
print(f"{n} X 3 = {n * 3}")
print(f"{n} X 4 = {n * 4}")
print(f"{n} X 5 = {n * 5}")
print(f"{n} X 6 = {n * 6}")
print(f"{n} X 7 = {n * 7}")
print(f"{n} X 8 = {n * 8}")
print(f"{n} X 9 = {n * 9}")
print(f"{n} X 10 = {n * 10}")

## 10. Develop a program that shows how many reais is possible to buy with the amonunt of money the user has
print('')
print("=== Convert dolars to reais ===")
d = float(input("Type how many dolars you want to convert: "))
conv_rate = 5.71
r = d * conv_rate
print(f"Considering the conversion rate of {conv_rate}, with {d} dolars you may buy {r:.2f} reais")

print('')
print("=== Convert reais to dolars ===")
r = float(input("Type how many reais you want to convert: "))
d = r / conv_rate
print(f"Considering the conversion rate of {conv_rate}, with {r} reais you may buy {d:.2f} dolars")