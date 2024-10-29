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
print(f"Your average is {m:.1f}")

## 8. Develop a program that reads a number in meters and converts it to centimeters and milimeters
print('')
print("=== Convert meters to cm and mm ===")
meter = float(input("Type a measure in meters: "))
cm = meter * 100 
mm = meter * 1000
print(f"{meter}m is equivalent to {cm:.0f}cm")
print(f"{meter}m is equivalent to {mm:.0f}mm")

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
d = float(input("Type how many dolars you want to convert: US$"))
conv_rate = 5.71
r = d * conv_rate
print(f"Considering the conversion rate of {conv_rate}, with {d} dolars you may buy {r:.2f} reais")

print('')
print("=== Convert reais to dolars ===")
r = float(input("Type how many reais you want to convert: R$"))
d = r / conv_rate
print(f"Considering the conversion rate of {conv_rate}, with {r} reais you may buy {d:.2f} dolars")

## 11. Develop a program that considering length and width of a wall, calculates its area and returns the amount of paint that is necessary to paint it. Consider that each liter of paint is enough to cover 2 square meters of wall
print('')
print("=== How much paint do I need? ===")
length = float(input("Type the length in meters: "))
width = float(input("Type the width in meters: "))
area = length * width
paint = area / 2
print(f"To paint {area} square meters, it is going to be necessary {paint} liters of paint")

## 12. Develop a program that given the price of an item, displays it with progressive discounts
print('')
print("=== Progressive discounts ===")
price = float(input("Type the price of the item: US$ "))
print(f"You will have a 5% discount if you buy two items and pay only {price * .95} each")
print(f"If you buy three items, we apply a 8% discount. You pay only {price * .92} each")
print(f"One item: {price}")
print(f"Two items: {(price * .95) * 2}")
print(f"Three items: {(price * .92) * 3}")

## 13. Develop a program that asks for the user income and shows how much he/she would make if given 15% raise
print('')
print("=== Happy raise ===")
wage = float(input("Type how much is your current wage: "))
print(f"If you have a 15% raise, your new wage will be {wage * 1.15}")

## 14. Develop a program that converts Celsius to Fahrenheight
print('')
print("=== Temperature conversion ===")
c = float(input("Type the temperature in Degrees Celsius: "))
convert_f = (c * 9 / 5) + 32 ## these parenthesis are optional
print(f"{c} ºC is equivalent to {convert_f:.1f} ºF")
print('')
f = float(input("Type the temperature in Degrees Fahrenheight: "))
convert_c = (f - 32) * 5 / 9
print(f"{f} ºF is equivalent to {convert_c:.1f} ºC")

##15. Develop a program that asks for the amount of km driven by a rental car and the amount of days it was rented for. Calculate the total amount for the rental, knowing that the car costs R$60 per day and R$0.15 per km
print('')
print("=== Rental car price ===")
days = int(input("Type the number of days with the car: "))
const_day = 60
km = float(input("Type the number of kilometers driven: "))
const_km = 0.15
print(f"The total cost for your rental will be US${(days * const_day) + (km * const_km)} dolars")