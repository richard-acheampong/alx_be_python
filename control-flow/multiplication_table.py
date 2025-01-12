
try:
    number = int(input("Enter a number to see its mulplication table: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Invalid number. Please enter a numeric value.")