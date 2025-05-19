#temperature converting function
def temp_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Is it (C)elsius or (F)arenheit?: ").upper()
    if unit == 'C':
        print(f"{temp} Celsius is {((temp * 9/5) + 32)} Farenheit")
    elif unit == 'F':
        print(f"{temp} Farenheit is {((temp -32) * 5/9)} Celcius")
    else:
        print("Invalid unit.")
        

#distance converting function
def distance_converter():
    dist = float(input("Enter distance: "))
    unit = input("Is it in (M)iles or (K)m?: ").upper()
    if unit == 'M':
        print(f"{dist} Miles is {dist * 1.60934} Kilometers")
    elif unit == 'K':
        print(f"{dist} Kilometers is {dist / 1.60934} Miles")
    else:
        print("Invalid unit.")
    
    
#weight converting function
def weight_converter():
    weight = float(input("Enter a weight: "))
    unit = input("Is it in K(g) or (L)bs? ").upper()
    if unit == 'K':
        print(f"{weight} Kilograms is {weight * 2.20462} Pounds")
    elif unit == 'L':
        print(f"{weight} Pounds is {weight / 2.20462} Kilograms")
    else:
        print("Invalid unit.")
    

#Main where the functions are called
while True:
    print("\n---- Unit Converter ----")
    print("1. Temperature \n2. Distance \n3. Weight \n4. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        temp_converter()
    elif choice == 2:
        distance_converter()
    elif choice == 3:
        weight_converter()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

