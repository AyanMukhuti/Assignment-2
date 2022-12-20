a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a+b>c and a+c>b and b+c>a:
    print("Yes, triangle can be formed.")
else:
    print("No, triangle cannot be formed.")


