print("Exercise 25 No of Days in a Month")


def No_of_Days(year, month):
    Leapyear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                Leapyear = True


        else:
            Leapyear = True

    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = 0

    if Leapyear == True:
        if month == 2:
            months[2] = 29
            days = months[month]
            print("Number of days is", days)
        else:
            days = months[month]
            print("Number of days is", days)
    else:
        days = months[month]
        print("Number of days is", days)


Year = int(input("Enter the Year: "))
Month = int(input("Enter the Month Number: "))
No_of_Days(Year, Month)
