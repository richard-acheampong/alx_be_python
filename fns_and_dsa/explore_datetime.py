from datetime import datetime, date, timedelta

def display_current_datetime():
    current = datetime.now()
    current_datetime = current.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_datetime)

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: ")) 
        future_date = date.today() + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")  
        print("Future date:", formatted_future_date)  
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
