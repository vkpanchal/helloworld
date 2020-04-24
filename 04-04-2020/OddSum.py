# Take input from user.
num = int(input("Print sum of Odd numbers till : "))

total = 0

for i in range(1, num + 1):

    # Check for even or not.
    if((i % 2) == 1):
        total = total + i
        print("Odd number",i);
        print("\nSum of Odd numbers from 1 to", num, "is :", total)