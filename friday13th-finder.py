from datetime import date

def day_of_week(y, m, d):
#   Determine the day of the week for a given date.
    try:
        # Create a date object
        date_obj = date(y, m, d)
        
        # List of weekday names
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[date_obj.weekday()]
    
    except ValueError:
        raise ValueError("Invalid date provided.")

def main():
    notdone = True;
    while(notdone):
        found = False
        print("Year (0=quit)? ", end="")
        theyear = int(input())
        if (theyear == 0):
            notdone = False
        else:
            for themonth in range(1, 13):        
                if day_of_week(theyear, themonth, 13) == "Friday":
                    print(f"{themonth}/13-{theyear} was/will be Friday the 13th")
                    found = True

            if not found:
                print(f"There were no Friday the 13ths in {theyear}")
            print()

if __name__ == "__main__":
    main()
