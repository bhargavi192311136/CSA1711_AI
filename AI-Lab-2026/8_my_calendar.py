import calendar

# Ask user for year and month
try:
    year = int(input("Enter year (e.g., 2026): "))
    month = int(input("Enter month (1-12): "))

    if 1 <= month <= 12:
        # Generate calendar
        cal = calendar.month(year, month)
        print("\nHere is the calendar:")
        print(cal)
    else:
        print("Invalid input! Month must be between 1 and 12.")

except ValueError:
    print("Invalid input! Please enter numbers only.")
