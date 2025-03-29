Homework 13 Datetime
Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import datetime, timedelta

def calculate_age(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
#     print(years)
# birthdate = input("Enter your birthdate (DD-MM-YYYY): ")   
# calculate_age(birthdate)
    if days < 0:
        months -= 1
        previous_month = today.replace(day=1) - timedelta(days=1)
        days += previous_month.day
    
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

birthdate = input("Enter your birthdate (DD-MM-YYYY): ")
try:
    years, months, days = calculate_age(birthdate)
    print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("You enterd wrong data")


Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
from datetime import datetime

def next_birthday(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    
    next_birthday = birth_date.replace(year=today.year)
    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_remaining = (next_birthday - today).days
    
    return days_remaining

birthdate = input("Enter your birthdate (DD-MM-YYYY): ")
try:
    days_left = next_birthday(birthdate)
    print(f"{days_left} days left to your birthday:)")
except ValueError:
    print("You entered wrong data")
Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

# Get current date and time from user
current_datetime_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")

# Get meeting duration
hours = int(input("Enter meeting duration (hours): "))
minutes = int(input("Enter meeting duration (minutes): "))

# Calculate end time
meeting_duration = timedelta(hours=hours, minutes=minutes)
end_datetime = current_datetime + meeting_duration

# Print the result
print("The meeting will end at:", end_datetime.strftime("%Y-%m-%d %H:%M"))

Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

# Get date, time, and timezone from user
current_datetime_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
current_timezone_str = input("Enter your current timezone (e.g., UTC, US/Eastern, Europe/London): ")
target_timezone_str = input("Enter the target timezone: ")

# Convert input to datetime object
current_timezone = pytz.timezone(current_timezone_str)
target_timezone = pytz.timezone(target_timezone_str)
current_datetime = current_timezone.localize(datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M"))

# Convert to target timezone
target_datetime = current_datetime.astimezone(target_timezone)

# Print the result
print("The converted date and time is:", target_datetime.strftime("%Y-%m-%d %H:%M %Z"))

5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
from datetime import datetime, timedelta
import time

# Get future date and time from user
future_datetime_str = input("Enter the future date and time (YYYY-MM-DD HH:MM): ")
future_datetime = datetime.strptime(future_datetime_str, "%Y-%m-%d %H:%M")

while True:
    # Get current time
    now = datetime.now()
    time_remaining = future_datetime - now
    
    # Check if the countdown has ended
    if time_remaining.total_seconds() <= 0:
        print("Countdown complete!")
        break
    
    # Extract remaining time components
    days, seconds = divmod(time_remaining.total_seconds(), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    
    # Print the countdown timer
    print(f"Time remaining: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds", end="\r")
    
    time.sleep(1)

Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re

def is_valid_email(email):
    # Regular expression pattern for validating email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

# Get email input from user
email = input("Enter your email address: ")

# Validate email
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address. Please enter a correct format.")

Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re

def format_phone_number(phone):
    # Remove non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Check if the number has exactly 10 digits
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return "Invalid phone number. Please enter a 10-digit number."

# Get phone number input from user
phone = input("Enter your phone number: ")

# Format and print the phone number
formatted_phone = format_phone_number(phone)
print("Formatted Phone Number:", formatted_phone)

Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re

def check_password_strength(password):
    # Define password criteria
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    
    # Determine overall strength
    errors = [length_error, uppercase_error, lowercase_error, digit_error]
    
    if any(errors):
        print("Weak password. Please ensure it:")
        if length_error:
            print("- Is at least 8 characters long")
        if uppercase_error:
            print("- Contains at least one uppercase letter")
        if lowercase_error:
            print("- Contains at least one lowercase letter")
        if digit_error:
            print("- Contains at least one digit")
    else:
        print("Strong password!")

# Get password input from user
password = input("Enter a password: ")
check_password_strength(password)

Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
import re

def find_word_occurrences(text, word):
    # Use regex to find all case-insensitive occurrences of the word
    matches = [match.start() for match in re.finditer(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)]
    
    if matches:
        print(f"The word '{word}' was found at positions: {matches}")
    else:
        print(f"The word '{word}' was not found in the text.")

# Sample text
sample_text = "This is a sample text. The word finder program will locate the word in this text. Finding words can be useful."

# Get word input from user
search_word = input("Enter a word to find: ")
find_word_occurrences(sample_text, search_word)

Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re

def extract_dates(text):
    # Regular expression to match dates in formats like DD/MM/YYYY, MM-DD-YYYY, YYYY.MM.DD
    date_pattern = r'\b(\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{4}[./-]\d{1,2}[./-]\d{1,2})\b'
    dates = re.findall(date_pattern, text)
    
    if dates:
        print("Dates found:", dates)
    else:
        print("No dates found in the text.")

# Get text input from user
user_text = input("Enter a text containing dates: ")
extract_dates(user_text)
