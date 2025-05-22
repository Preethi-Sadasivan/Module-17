# Get year from user
year = int(input("Enter a year: "))

# Check leap year logic directly
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
