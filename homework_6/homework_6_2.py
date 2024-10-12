while True:
    entered_string = input("Please enter a number in diapason 0 ≤ N < 8640000, where 'N' is the entered number: ")

    # Checking if the entered string is a number
    if not entered_string.isdigit():
        print("Entered not a number!")
    else:
        # Converting entered to an integer var & checking the diapason
        entered_number = int(entered_string)
        if not 0 <= entered_number < 8640000:
            print("The entered number is out of the diapason!")
        else:
            # By using divmod() method defining days, hours, minutes, seconds of the entered number
            days, remained_seconds = divmod(entered_number, 86400)
            hours, remained_seconds = divmod(remained_seconds, 3600)
            minutes, seconds = divmod(remained_seconds, 60)
            print(f"The result is: {days} day(s), {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    to_continue = input("Please enter 'q' to quit or anything else to continue: ")
    if to_continue == "q":
        break
