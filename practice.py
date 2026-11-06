'''names = ["Alice", "Bob", "Charlie"]'''

'''print(names[-3])
print(names[-2])
print(names[-1])'''

'''cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

my_cart = cart + fav_items
print(my_cart)'''


'''names[1] = "Rinah"
print(names)'''

'''names.append("David")
print(names)


names.insert(2, "Eve")
print(names)'''


'''favorite_items = ['T-shirt', 'Lamp', 'Pen', 'Book']
favorite_items.remove('Lamp')
cart = favorite_items.copy()

print(cart)

numbers = {4, 6, 6, 2, 8, 2}
print(numbers)   # {8, 2, 4, 6}

numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) '''


'''country = {"Germany": "Berlin", "Uganda": "Kampala", "Kenya": "Nairobi"}
print(country)'''

def add(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum
    sum = add(5, 10, 18)
    print("The sum is:", sum)
result = add(5, 10, 15)
print("The result is:", result)


class People:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
Greet=(People())
People1 = People()
Greet.name = "Rinah"
Greet.age = 20
People1.name = "Alice"
People1.age = 25
print(Greet.name, Greet.age)
print(People1.name, People1.age)
    