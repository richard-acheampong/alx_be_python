#  Utilize Python lists to create a simple shopping list manager that allows 
# users to add items,view the current list, and remove items.

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            item = input("Enter item: ").strip() #strip removes any leading or trailing white spaces
            shopping_list.append(item) #adds the item to the list

        elif choice == "2":
            item = input("Enter item: ").strip()
            shopping_list.remove(item) #removes the item from the list
            
        elif choice == "3":
            print(shopping_list) #prints the list
        elif choice == "4":
            break #end the loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


