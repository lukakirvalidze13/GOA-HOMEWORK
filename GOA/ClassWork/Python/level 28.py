numbers = [1,3,5,7,9,11]
numbers.append(5)
numbers.pop(3)
numbers.insert(1, "10")
print(numbers) 



def greet(first_name, last_name):
    return "Hello" + " " + first_name + " " + last_name

message = greet("Lu", "Na")

print(message)