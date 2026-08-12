print("Welcome to Unit Converter!")
print("\n1. Length")
print("2. Weight")
print("3. Temperature")
choice = int(input("\nEnter your choice: "))
if choice == 1:
    print("You have selected Length")
    choose = input("Choose an option: (A) Miles or (B) Kilometers: ").strip().upper()
    if choose == "A": 
        print("You have selected Miles")
        try:
            ask_user = float(input("Enter the Length in Miles: "))
            Kilometer = ask_user * 1.609
            print(f"Your Length is {Kilometer} kilometers")
        except ValueError:
            print("You have entered invalid number. Please enter a valid number")
    elif choose == "B":
        print("You have selected Kilometers")
        ask_user = float(input("Enter the Length in Kilometers: "))
        Mile = ask_user / 1.609
        print(f"The Length is {Mile} Miles.")
    else:
        print("You have selected Invalid option. Please select A or B")
elif choice == 2 :
    print("You have selected Weight")
    choose = input("Choose an option: (A) Kilograms or (B) Pounds: ").strip().upper()
    if choose == "A":
        print("You have selected Kilograms")
        ask_user = float(input("Enter the weight in Kilograms: "))
        Pound = ask_user * 2.2046
        print(f"The weight is {Pound} Pounds")
    elif choose == "B":
        print("You have selected Pounds")
        ask_user = float(input("Enter the weight in Pounds: "))
        Kilogram = ask_user * 0.4536
        print(f"The weight is {Kilogram} Kilograms")
    else:
        print("You have selected Invalid option. Please select A or B")
elif choice == 3 :
    print("You have selected Temperature")
    choose = input("Choose an option: (A) Fahrenheit or (B) Celsius: ").strip().upper()
    if choose == "A":
        print("You have selected Fahrenheit")
        ask_user = float(input("Enter the temperature in Fahrenheit: "))
        Celsius = (ask_user - 32) / 1.8
        print(f"The temperature is {Celsius} Celsius")
    elif choose == "B":
        print("You have selected Celsius")
        ask_user = float(input("Enter the temperature in Celsius: "))
        Fahrenheit = (ask_user * 1.8) + 32
        print(f"The temperature is {Fahrenheit} Fahrenheit")
    else:
        print("You have selected Invalid option. Please select A or B")
else:
    print("The given option is Invalid. Please select between 1, 2 or 3.")