# name = str(input("Enter your name "))
# surname =str( input("Enter your surname "))
# age =int(input("Enter your age "))
# height =float( input("Enter your height"))

# print(name)
# print(surname)
# print(age)
# print(height)



# #converter examples

# print(int("69"))
# print(int(69.3))
# print(float(69.9))

# 
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))

# sum = num1+num2+num3
# arithmetic = sum / 3
# print(arithmetic)



#calculator

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

operator = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("ჯამი:", result)
elif operator == "-":
    result = num1 - num2
    print("შესაფერისი სხვაობა:", result)
elif operator == "*":
    result = num1 * num2
    print("გამრავლებელი:", result)
elif operator == "/":
    if num2 != 0:  
        result = num1 / num2
        print("ნაწილება:", result)
    else:
        print("გთხოვთ, არ გამყოფოთ ნულზე!")
else:
    print("შეყვანილი ოპერატორი არასწორია!")