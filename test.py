print('')
print("=== Rental car price ===")
days = float(input("Type the number of days with the car: "))
const_day = 60
km = float(input("Type the number of kilometers driven: "))
const_km = 0.15
print(f"The total cost for your rental will be US${(days * const_day) + (km * const_km)} dolars")
