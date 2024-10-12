while True:
    entered_number = input("Please enter a number or 'q' to quit: ")

    if entered_number == "q":
        break
    # Checking if the entered string is a number
    elif not entered_number.isdigit():
        print("Entered not a number!")
    else:
        # Declaring a string and assigning there the entered string
        # Each new iteration the string is going to be set as intermediate result of the processed_number below
        processed_string = entered_number
        while True:
            # Declaring an integer for intermediate result
            # Each new iteration the integer is going to be set to 1
            processed_number = 1
            for digit in processed_string:
                # Multiplying each digit in the number and assigning it to the integer
                processed_number *= int(digit)
            # If the integer after the multiplication is less than 10, escaping from the loop
            if processed_number < 10:
                break
            # Else assigning the integer to the string and proceeding to the next iteration
            else:
                # Printing intermediate result just for easier debugging
                print(f"The number after an iteration is {processed_number}")
                processed_string = str(processed_number)

        print(f"The result number after all iterations is {processed_number}")
