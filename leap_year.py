while True:
    # get year from user, reprompt if not an inta
    while True:
        try:
            year = int(input("Enter a year: "))
        except:
            print ("Input error: letters or special characters are not accepted. Please try again.")
            continue
        if year < 0:
            print("Input error: letters or special characters are not accepted. Please Try again.\n")
            continue
        
        else:
            break

    # if a year is divisible by 4 = leap year
    # if a year is divisible by 4 but not 100 = leap year
    # if a year is divisible by 100 but not 400 = not a leap year
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0:
                print (str(year) + " is a leap year")
            else:
                print (str(year) + " is not a leap year")
        else:
            print (str(year) + " is a leap year")
    else:
        print (str(year) + " is not a leap year")
