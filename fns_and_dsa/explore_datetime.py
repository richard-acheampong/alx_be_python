from datetime import datetime, date, timedelta

def display_current_datetime():
    current = datetime.now()
    current_datetime = current.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_datetime)

def calculate_future_date():
    day = int(input("Enter number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=day)
    print("Future date: ", future_date)

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()  