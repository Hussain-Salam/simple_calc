#Simple Calculator
#S M Hussain Salam
#12/12/18

loop = 1
print("Choose a following option from the list belows: \n1. Add \n2. Subtract \n3. Divide \n4. Multiply \n5. Exit\n\n")
while loop == 1:
    chosen_option = int(input("Choose a following option (1-5): "))
    if chosen_option == 5:
        loop=loop-1
        print("Program terminated.")
    else:
        first_number = int(input("Choose your first number: "))
        second_number = int(input("Choose your second number: "))
        if chosen_option == 1:
            print(first_number,"+" , second_number,"=",first_number+second_number)
        elif chosen_option == 2:
            print(first_number,"-" , second_number,"=",first_number-second_number)
        elif chosen_option == 3:
            print(first_number,"÷" , second_number,"=",first_number/second_number)
        elif chosen_option == 4:
            print(first_number,"×" , second_number,"=",first_number*second_number)
        else:
            print("ERROR: Unknown command.")
