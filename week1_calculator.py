a= float(input("enter first number:"))
b= float(input("enter second number:"))
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice = int(input("Choose (1-4): "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    print("Result:", a / b)
else:
    print("Invalid choice")