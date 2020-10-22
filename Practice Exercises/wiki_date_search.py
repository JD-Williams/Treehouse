import datetime
import calendar
import webbrowser

def greeting():
    print("""
        Welcome to the 'ON THIS DAY' application.

        Use this app to search Wikipedia for any special events
        that occured on the date you provide. Have fun!
    """)

def validate_year():
    current_year = datetime.date.today().year
    while(True):
        try:
            year = int(input("Enter a positive integer for any year up to the present: "))
        except ValueError:
            print("This is not a number. Please try again.\n")
        else:
            if(year > 0 and year <= current_year):
                break
            print(f"The input \'{year}\' is invalid. Please try again.\n")
    return year

def print_months():
    for num, month in enumerate(calendar.month_abbr):
        if(num != 0):
            print(f"{num:>2}: {month}")
    print()

def validate_month():
    # print_months()
    while(True):
        month = input("Enter the 3-letter abbreviation for the month (ex. Jan, Feb, etc): ").title()
        if(month in calendar.month_abbr):
            break
        print(f"The input \'{month}\' is invalid. Please try again.\n")
    month_num = datetime.datetime.strptime(month, "%b").month
    return month_num

def validate_day(year, month):
    """Determines whether a day exists for year, month"""
    specific_month = datetime.datetime.strftime(datetime.date(year, month,1), "%B %Y")
    max_days = calendar.monthrange(year, month)[1] # the maximum number of days in the specified month
    while(True):
        try:
            day = int(input(f"Enter an integer for a day in {specific_month}: "))
        except ValueError:
            print("This is not a number. Please try again.\n")
        else:
            if(day > 0 and day <= max_days):
                break
            print(f"There are only {max_days} days in {specific_month}, not \'{day}\'.")
            response = input("Enter '0' to start over, otherwise press any other key. ")
            print()
            if(response == "0"):
                return False
    return day

def get_date():
    while(True):
        year = validate_year()
        print()
        month = validate_month()
        print()
        day = validate_day(year, month)
        if(isinstance(day, bool)):
            print()
            print()
            continue
        else:
            print()
            print(f"The date you selected is {month}/{day}/{year}.")
            response = input("Enter '0' to start over, otherwise press any other key. ")
            if(response == "0"):
                continue
            break
    return datetime.date(year, month, day)

def open_webpage(datetime_object):
    url_format = '%b_%d'
    date_format = datetime.datetime.strftime(datetime_object, url_format)
    url = f'https://en.wikipedia.org/wiki/{date_format}'
    webbrowser.get("macosx").open(url, new=1)

def search_wikipedia():
    greeting()
    search_date = get_date()
    open_webpage(search_date)

search_wikipedia()
