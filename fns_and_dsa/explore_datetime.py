import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time: {}"
            .format(current_date.strftime("%Y-%m-%d %H:%M:%S")))

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to "
                            "the current date: "))
    today = datetime.date.today()
    future_date = datetime.timedelta(days=number_of_days) + today
    print(f"Future date: {future_date}")
