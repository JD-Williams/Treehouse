import datetime
import pytz
import random

random.seed(917)
fmt = "%Y-%m-%d %H:%M %Z%z"

def get_date():
    while(True):
        date_input = input("Enter the date and time of your meeting. Use the MM/DD/YYYY HH:MM format. ")
        try:
            local_date = datetime.datetime.strptime(date_input, "%m/%d/%Y %H:%M")
        except ValueError:
            print(f"Your input of \'{date_input}\' is not valid. Please try again.\n")
        else:
            local_date = pytz.timezone("US/Eastern").localize(local_date)
            utc_date = local_date.astimezone(pytz.utc)
            break
    return utc_date

def count_of_tzs():
    while(True):
        try:
            count = int(input("Enter the number of timezones for conversion: "))
        except ValueError:
            print("This is not an integer. Please try again.\n")
        else:
            if(count >0 and count <= len(pytz.all_timezones)):
                break
            print(f"The input \'{count}\' is invalid. Please try again.\n")
    return count

def generate_random_tzs():
    tzs = []
    number_of_tzs = count_of_tzs()
    for _ in range(number_of_tzs):
        tzs.append(random.choice(pytz.all_timezones))
    return tzs

def print_date_in_tzs(dt, tzs):
    print(f"The following are {len(tzs)} equivalent dates in differnt timezones:")
    for tz in tzs:
        print(f" * {dt.astimezone(pytz.timezone(tz))} <--> {tz}")

def convert_datetime():
    utc_date = get_date()
    print(f"The UTC date you selected is {utc_date}.")
    print()
    timezones = generate_random_tzs()
    print()
    print_date_in_tzs(utc_date, timezones)

convert_datetime()
