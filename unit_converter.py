print("Welcome to Unit Converter!")
print("\n1. Length")
print("2. Weight")
print("3. Temperature")
choice = int(input("\nEnter your choice: "))
if choice == 1:
    print("You selected Length")
elif choice == 2 :
    print("You selected Weight")
elif choice == 3 :
    print("You selected Temperature")
else:
    print("The given number is not valid.")