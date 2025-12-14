# # # hash symbol - დიეზი # 
# # # underscore - ქვედატირე _
# # # Displaying - გამოტანა, ერკანზე გამოსახულების გამოტანა
# # # Declaring - შექმნა, გამოცხადება
# # # good practice - კარგი პრაქტიკა
# # # comments - კომენტარი
# # # instruction - დავალება
# # # case-sensitve - ქეისისადმი (დიდი-პატარა ასოების) მგრძნობიარე
# # # uppercase - დიდი ასოები
# # # lowercase - პატარა ასოები

# # # Output - გამოტანა
# # # Input - შეტანა
# # # Data Types - მონაცემთა ტიპები
# # # string - ტექსტური მონაცემი, რომელიც იწერება ბრჭყალებში
# # # integer - მთელი რიცხვი
# # # join - გაერთიანება, შესვლა
# # # add - დამატება
# # # insert - ჩასმა
# # # concatenation - string ტიპის მონაცემების გაერთიანება


# # b1 = 5.50
# # b2 = 9.50   
# # b3 = 10.50
# # b4 = 25
# # b5 = 35

# # discount = 3.50

# # nb1 = (b1-discount)
# # nb2 = (b2 - discount)
# # nb3 = (b3 - discount)
# # nb4 = (b4 - discount)
# # nb5 = (b5 - discount)
# # print("New prices for 5 books available for today : ",nb1,nb2,nb3,nb4,nb5)

# # name = input(str("Enter your name: "))
# # surname = input("Surname: ")
# # age = input("Enter your age: ")
# # location = input("Location: ")
# # occupation = input("Occupation: ")
# # hobby = input("Hobby: ")

# # print(name + " " + surname + " is " + age + " years old, " + " works as an " + occupation + "," + " and enjoys" +" "+ hobby)



# # 5) შექმენით 10 string ტიპის და 10 ინტეჯერ ტიპის ცვლადი, 
# # გააკეთეთ 5 კონკატინაციისა (სტრინგების შეერთების) და 5 მათემატიკური ჯამის მაგალითი

# a = "Hello "
# b = "There "
# c = "Beautiful "
# d = "Lady "
# e = "What "
# f = "Are "
# g = "You "
# h = "Up "
# i = "To "
# j = "Cutie "


# result = a + b + c + d + e + f
# print(result)

# x = 50
# y = 50
# result = x * y
# print(result)


# # integer = mteli ricxvebi მაგალითად 69
# # float = წილადი რიცხვები მაგალითად 2.69


# x = 2
# y = 2
# b = 2.69
# answer = x * (y + b)
# print(answer)


# #8) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას,
# # შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.

# # x = "x5"
# # y = 69
# # print(type(x))
# # print(type(y))



# 9) თიოთეული მონაცემთა ტიპისთვის (str,int,float),
#შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი

# str = "Hello there"
# print(type(str))

# float = 1.5
# print(type(float))


# 11) მომხმარებელს შემოატანინეთ თავისი ასაკი, შემდეგ შემოატანინეთ წლების რაოდენობა.
#მიღებული ინფორმაცია შეინახეთ ცვლადებში და გამოითვალეთ,
#რამდენი წლის იქნება მომხმარებელი y (მომხმარებლის მიერ შემოტანილი) წლის შემდეგ.
#საბოლოოდ გამოუტანეთ შედეგი შემდეგი სახით: "[წლები] წლის შემდეგ თქვენ იქნებით [მომავალი ასაკი] წლის".
#დავალების შესასრულებლად გამოიყენეთ მონაცემთა ტიპების ხელოვნურად შეცვლის მეთოდები: int() -
#რომ შეასრულოთ ართიმეტიკული მოქმედებები, str() - რომ დაბეჭდოთ შედეგი შეცდომების გარეშე


# age = int(input("How old are you: "))
# # print("You are " + age + " years old")
# random_years = int(input("Choose a random number: "))
# answer = (age + random_years)
# print("In " + str(random_years) + " You will be " + str(answer) + " years old")


x = 5
y = 59
print("I'm a " + str(x))

a = "pumpkin"
b = "snow"
c = "ball"
print(b + c)

distance = 15
unit = "km"
print(str(distance) + unit)

print(25 < 20)
print(25 > 20)