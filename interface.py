Menu = True

print("Welcome to the Freight Manager")

while Menu:
    print("1. Add a box type")
    print("2. Show box type")
    print("3. Load box to container")
    print("4. Show Container")
    print("5. Summary report")
    print("X. Close")
    menu_user_input = input("Please select an option :")

    if menu_user_input == 'x':
        Menu = False
        print("Goodbye !")
    else:
        print(f"Option slected {menu_user_input}")




