print("Welcome to Unit Converter!")
print("\n1. Length")
print("2. Weight")
print("3. Temperature")
choice = int(input("\nEnter your choice: "))
if choice == 1:
    print("You selected Length")
    choose = input("Choose an option: (A) Miles or (B) Kilometers: ").strip().upper()
    if choose == "A": 
        print("You have selected Miles")
        ask_user = int(input("Enter the number of Miles: "))
        Kilometer = ask_user * 1.609
        print(f"Your answer is {Kilometer} kilometers")

elif choice == 2 :
    print("You selected Weight")
elif choice == 3 :
    print("You selected Temperature")
else:
    print("The given number is not valid.")