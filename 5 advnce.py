# Create a dictionary for months and their days
month_days = {
    1: 31,  # January
    2: 28,  # February (default, will adjust for leap years)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Ask user for month number
month_number = int(input("Enter the month number (1-12): "))

# Check if the input is valid
if 1 <= month_number <= 12:
    if month_number == 2:  # Check for February
        leap_year = input("Is this year a leap year? (yes/no): ").strip().lower()
        if leap_year == "yes":
            days = 29
        else:
            days = month_days[month_number]
   
    
    print("The number of days in month {month_number} is: {days}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
