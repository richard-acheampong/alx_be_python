#  Utilize Python lists to create a simple shopping list manager that allows 
# users to add items,view the current list, and remove items.

# def display_menu():
#     print("Shopping List Manager")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. View List")
#     print("4. Exit")


# def main():
#     shopping_list = []
#     while True:
#         display_menu()
#         choice = input("Enter choice: ").strip()
#         if choice == "1":
#             item = input("Enter the item to add: ") 
#             shopping_list.append(item) #adds the item to the list

#         elif choice == "2":
#             item = input("Enter the item to remove: ")
#             shopping_list.remove(item) #removes the item from the list
            
#         elif choice == "3":
#             print(shopping_list) #prints the list
#         elif choice == "4":
#             break #end the loop
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View List")
    print("4. Exit")


# def main():
#     shopping_list = []
#     while True:
#         display_menu()
#         choice = input("Enter choice: ").strip()
#         if choice == "1":
#             item = input("Enter the item to add: ")  # Exact match with checker
#             shopping_list.append(item)  # Adds the item to the list

#         elif choice == "2":
#             item = input("Enter the item to remove: ").strip()  # Clarify action
#             if item in shopping_list:
#                 shopping_list.remove(item)  # Removes the item from the list
#             else:
#                 print(f"'{item}' not found in the list.")

#         elif choice == "3":
#             if shopping_list:
#                 print("Current shopping list:")
#                 for idx, item in enumerate(shopping_list, 1):
#                     print(f"{idx}. {item}")
#             else:
#                 print("Shopping list is empty.")

#         elif choice == "4":
#             print("Exiting the Shopping List Manager.")
#             break  # End the loop
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        match choice:
            case "1":
                item = input("Enter the item to add: ")  # Exact match with checker
                shopping_list.append(item)  # Adds the item to the list

            case "2":
                item = input("Enter the item to remove: ").strip()  # Clarify action
                if item in shopping_list:
                    shopping_list.remove(item)  # Removes the item from the list
                else:
                    print(f"'{item}' not found in the list.")

            case "3":
                if shopping_list:
                    print("Current shopping list:")
                    for idx, item in enumerate(shopping_list, 1):
                        print(f"{idx}. {item}")
                else:
                    print("Shopping list is empty.")

            case "4":
                print("Exiting the Shopping List Manager.")
                break  # End the loop
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()