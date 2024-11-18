menu_option = ''
while menu_option != 'q':
    print(f"""
    Street Burger's Menu:
    a - Regular Burger
    b - Cheese Burger
    c - Bacon Cheese Burger 
    d - Double Cheese Burger
    e - Double Bacon Cheese Burger
    
    Enter a letter (or 'q' to quit):
    """)

    menu_option = input("> ")
    
    if menu_option == 'q':
        print("Goodbye!")
        break
    
    # Nested while loop for order confirmation
    while True:
        if menu_option == 'a':
            print("You ordered a Regular Burger!")
        elif menu_option == 'b':
            print("You ordered a Cheese Burger!")
        elif menu_option == 'c':
            print("You ordered a Bacon Cheese Burger!")
        elif menu_option == 'd':
            print("You ordered a Double Cheese Burger!")
        elif menu_option == 'e':
            print("You ordered a Double Bacon Cheese Burger!")
        else:
            print("Invalid option. Please choose from the menu.")
            break

        # Ask for confirmation
        confirm = input("Do you want to confirm your order? (y/n): ")
        if confirm.lower() == 'y':
            print("Order confirmed! Preparing your burger...\n")
            break
        elif confirm.lower() == 'n':
            print("Let's choose again!\n")
            break
        else:
            print("Invalid input, please enter 'y' or 'n'.")

print("Thank you for visiting Street Burger!")