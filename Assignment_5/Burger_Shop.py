#Assignment 5
menu_option = ''
while menu_option != 'q':
    print(f"""
    Street Burger's Menu:
    a - Regular Burger
    b - Cheese Burger
    c - Bacon Cheese Burger 
    d - Double Cheese Burger
    e - Double Bacon Cheese Burger
    
    Please eneter a letter:
    """)

    menu_option = input(">")
    if menu_option =='a':
        print("You ordered a Regular Burger!")
    
    elif menu_option == 'b':
        print("You ordered a Cheese Burger!")

    elif menu_option == 'c':
        print("You ordered a Bacon Cheese Burger!")

    elif menu_option == 'd':
        print("You ordered a Double Cheese burger!")
    
    elif menu_option == 'e':
        print("You ordered a Double Bacon Cheese Burger!")
        

        