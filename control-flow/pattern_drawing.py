size = int(input("Enter the size of the pattern: "))
while size < 1:
    size = int(input("Enter a positive number: "))

for i in range(size):
    for j in range(size):
        print("*", end=" ")
        # print("*")
    print()

