print("----------------------")
print("Welcome to Calculator")
print("----------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("What you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#choice = int(input("Enter your choice: "))
choice = input("Enter your choice (1/2/3/4) : ")

if choice == "1" :
     result = num1 + num2
     print("num1 + num2 = " , result)
elif choice == "2" :
     result = num1 - num2
     print("num1 - num2 = " , result)
elif choice == "3" :
    result = num1 * num2
    print("num1 * num2 = " , result)
elif choice == "4":
    if num2 == 0:
        print("Error! Cannot divide by zero.")
    else:
        result = num1 / num2
        print("num1 / num2 " , result)
else:
        print('Invalid choice! Please enter 1, 2, 3 or 4.')

print ("Thank You For Using My calculator .")

