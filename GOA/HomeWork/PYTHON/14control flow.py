# solve problem - პროგრამის მოგვარება
# control flow - დინების მართვა
# techniques - ტექნიკები
# sequence - თანმიმდევრობა
# iteration - გამეორება
# selection - შერჩევა
# order - თანმდიმდევრობა
# top - ზემოთ
# bottom - ქვემოთ
# repeat - გამეორება
# algorithm - ნაბიჯ-ნაბიჯ ინსტრუქციები
# follow path - გზას გაყოლა
# notify - შეტყობინება
# range - დიაპაზონი
# represent - წარმოდგენა
# flowchart - დიაგრამა
# pseudocode - ფსევდოკოდი
# natural language - ბუნებრივი გზა
# different ways - სხვადასხვანაირად
# range - დიაპაზონი
# loop - მარყუჟი, ციკლი, გამეორება
# iteration - გამეორება
# keyword - რეზერვირებული სიტყვა ენაში
# iterable - პროგრამირებაში დალაგებული მიმდევრობა
# sum - ჯამი
# while - რაღაცის განმავლობაში, იქამდე სანამ
# infinite - უსასრულო
# condition - პირობა
# initial  - საწყისი


#1 control flow has three techniques, Sequencing, Iteration, Selection.   
# Iteration - It's about executing an instruction repeatedly. it's commonly represented as a loop for example
# for num in range(5):
#     print(num)

# name = "Luka"
# for char in "Luka":
#     print(char)

# #2 Selection - Specifies when to follow each path.
# #3 sequencing - runs the code in sequence for example from top to bottom.

# #Algorithms - set of instructions to complete a task placed in a certain order.

# for num in range(1,31):
#     print(num)

# for number in range(15,81):
#     print(number)

# for num in range(89):
#     print(num)

# for num in range(0,51,3):
#     print(num)


# number = int(input("First number "))
# number_2 = int(input("Second number "))
# # for num in range(number,number_2 +1):
# #     print(num)

# # for num in range(0,101,2):
# #     print(num)

# # for sum in range(20,40):
# #     print(sum + sum)


# # #factorial of 7

# # import math
# # n = 7
# # print(math.factorial(n))

# n = 7
# f = 1
# for num in range(n, 1, -1):
#     # print(num)
#     f = f * num
    
# print(f)

# # x = 20
# # while x>=0:
# #     print(x)
# #     x-=1


# x = 0
# while x<=20:
#     print(x)
#     x+=1

# x = 10
# while x <= 30:
#     print(x)
#     x+=1

# n = 15
# while n < 80:
#     print(n)
#     n+=1

# y = 69
# while y >= 0:
#     print(y)
#     y = y-5

# x = 50
# while x >= 0:
#     print(x)
#     x-=3

# x = 0   
# while x <=50:
#     print(x)
#     x+=1

# x = 100
# while x >= 20:
#     print(x)

# password = "luna"
# pass_input = input("Enter your password :")
# tries = 10
# while pass_input != password:
#     pass_input = (input("Enter again : "))
#     tries-=1
# print("Authorised successfully")

# pin_code = "salam"
# tries = 3
# code= ""
# while code!=pin_code:
#     code = input("Enter your code: ")
#     tries -=1
# print("Ok")

# default = "luna_x5"
# user_input = ""
# tries = 3
# while user_input!=default:
#     user_input=input("PASSWORD > ")
#     tries-=1

# print("OK")

# code = "6969"
# password = ""
# tries = 5
# while password != code :
#     password = input("PASSWORD > ")
#     tries-=1
    
# print("You took "+ str(tries))


fruits = ["Banana", "Apple", "Pineapple", "cherry"]
for x in fruits:
    if x == "Banana":
        continue
    elif x == "Apple":
        continue
    print(x)

top = "BMW", "X5", "X7"
Luxury = "X7", "Range rover"
for x in top:
    for y in Luxury:
        print(x,y)


for x in [1,3,5,7]:
    print(x)

i = 0
while i<=69:
    print(i)
    i+=1