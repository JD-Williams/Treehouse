import datetime
import pytz
import random

fmt = "%Y-%m-%d %H:%M %Z%z"
tz_country_dict = {country:tzs for country,tzs in pytz.country_timezones.items()}
country_abbr = sorted(list(tz_country_dict.keys()))

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

def print_country_tzs(country):
    for idx, tz in enumerate(pytz.country_timezones(country)):
        print(f"{idx+1:>02} - {tz}")

def add_timezone():
    while(True):
        country = input("Enter the country abbreviation for the timezone (ex. US, CA): ")
        if not(country in country_abbr):
            print("This is not a valid country. Please try again.\n")
            continue
        else:
            tzs_in_country = len(pytz.country_timezones(country))
            print(f"There are {tzs_in_country} timezones in {country}.")
            print_country_tzs(country)
            while(True):
                try:
                    tz_idx = int(input("Enter the ID for the desired timezone: "))
                except ValueError:
                    print("This is not a number. Please try again.\n")
                else:
                    if tz_idx not in range(1, tzs_in_country + 1):
                        print("This is not a valid timezone ID.\n")
                        continue
                    break
            return pytz.country_timezones(country)[tz_idx - 1]            

def get_user_tzs():
    user_tzs = [] 
    add_more = True
    print(f"There are a total of {len(country_abbr)} countries to choose from.")
    display_tz_countries = input("Do you want to view a list of all possible timezone countries? (yes/no): ").lower()
    if display_tz_countries == "yes":
        for abbr, tzs in tz_country_dict.items():
            print(f"{abbr} - ",end="")
            print(*tzs, sep=", ")
        print()
    while(add_more):
        user_tzs.append(add_timezone())
        try:
            add_more = int(input("Do you want to add another timezone? Enter \'1\' for yes and \'0\' for no. "))
        except ValueError:
            print("This is not a number. Please try again.\n")
        else:
            if not(add_more in range(2)):
                print("Your selection is invalid. Please try again.\n")
            print()
    return user_tzs

def generate_random_tzs():
    random_tzs = []
    number_of_tzs = count_of_tzs()
    for _ in range(number_of_tzs):
        random_tzs.append(random.choice(pytz.all_timezones))
    return random_tzs

def print_date_in_tzs(dt, tzs):
    print(f"The following are {len(tzs)} equivalent dates to {dt} in different timezones:")
    for tz in tzs:
        print(f" * {dt.astimezone(pytz.timezone(tz))} <--> {tz}")

def convert_datetime():
    # tz_selection = 0
    utc_date = get_date()
    print(f"The UTC date you selected is {utc_date}.")
    print()
    print()
    while(True):
        try:
            tz_selection = int(input("Enter \'1\' to select your own timezones or \'2\' to generate random timezones: "))
        except ValueError:
            print("This is not a number. Please try again.\n")
        else:
            if not(tz_selection in range(1,3)):
                print("Your selection is invalid. Please try again.\n")
            elif tz_selection == 1:
                timezones = get_user_tzs()
                break
            else:
                timezones = generate_random_tzs()
                break
    print()
    print_date_in_tzs(utc_date, timezones)

convert_datetime()
