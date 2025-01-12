def main():
    task = input("Enter your task: ")
    priority = input("Priority (high, medium, low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}'  a high priority task. Consider completing it as soon as possible.")
    
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires attention today!.")
            else:
                print(f"Note: '{task}' is a medium priority task. Consider completing it when you have the time.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires attention today!.")
            else:
                print(f"Note: '{task}'  a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

if __name__ == "__main__":
    main()