from datetime import datetime

# --- Step 1: Ask user for birthdate ---
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

try:
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
except ValueError:
    print(" Invalid format. Please use DD/MM/YYYY.")
    exit()

# --- Step 2: Calculate age ---
today = datetime.today()
age = today.year - birthdate.year

# Fix if birthday hasn't happened yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# --- Step 3: Find number of candles ---
candles = age % 10  # last digit of age
if candles == 0:
    candles = 1  # at least 1 candle :)

# Create candles row
candles_row = " " * 7 + "i" * candles + " " * 7

# --- Step 4: Draw cake ---
cake = f"""
       ___{ "i" * candles }___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# --- Step 5: Check leap year ---
year = birthdate.year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Print cake(s)
print("\n Happy Birthday! You are", age, "years old today! \n")
print(cake)
if is_leap:
    print("Wow! You were born in a leap year  So you get TWO cakes!\n")
    print(cake)
