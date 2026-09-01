 # Object Oriented Programming
#Focus on real life entities to write code

#Object - Any real Life entity represented in code
#for example - student, cars, fruits

#Class - Blueprint of an object
#(apple, banana, mango ) (objects) - > Fruits (class)

# https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/

class Fruit:
    # attributes / properties of class
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference
        #self.sample = sample
      
      #  Class Methods

      # Getters - to get the values
    def get_shape(self):
        return self.shape

      # Setters -  to set or chg the values 
    def set_shape(self, new_shape):
        self.shape = new_shape

      # Custom Methods
    def increase_preference(self):
        self.preference = self.preference + 1

    def showFruit(self):
        print(f"\nHello I am a fruit with {self.color}, {self.shape}, {self.taste}, {self.preference}")

#object1 creating
print()
    # values can be gvn in any order as all r string values
    # but the order of parameters in constructor should be same as defined in class
apple = Fruit("red", "sour", "round",1) #(color,taste,shape, preference)
apple.showFruit()

# to get only any 1 value(let's say only the shape of apple)
print(f'Get the shape of fruit = {apple.get_shape()}\n')# get_shape() func. called to get the shape
apple.increase_preference() # call func. to inc. preference

apple.set_shape("sphere")  # set the value of shape
apple.showFruit()
print(f'\n-----------------------\n')

#object 2
banana = Fruit("yellow", "sweet", "cylinder",1)
banana.showFruit()
banana.increase_preference()
banana.showFruit()
print(f'Get the shape of fruit = {banana.get_shape()}\n')

"""Project Description
This project showcases the implementation of the concepts of OOP like 
classes, objects, attributes, and methods."""

""" H.W.
Additional Practice:

Practice 1: The Student Profile

Task: Create a class to represent a Student in a school system.

Class Name: Student
Attributes: name, grade, school_name.
Methods:
show_details(): Prints a sentence like "I am [name] from [school] in grade [grade]."
Logic Hint (Give if needed): Create two different student objects (e.g., "John" and "Alex") and call show_details() for both.
Practice 2: The Racing Car (Changing State)

Task: Create a car that can speed up and slow down.

Class Name: Car
Attributes: brand, speed (start speed at 0).
Methods:
accelerate(): Increases speed by 10. Print "Vroom! Speed is noPractice 3: The Bank Account (Logic & Validation)

Task: Create a secure bank account system.

Class Name: BankAccount
Attributes: account_holder, balance.
Methods:
deposit(amount): Adds money to the balance.
withdraw(amount): Subtracts money only if balance >= amount. If not, print "Insufficient Funds!".
check_balance(): Prints the current balance.
Logic Hint (Give if needed): Try to withdraw more money than you have to test the protection logic.
Practice 4: The "Smart" Smartphone (Getters & Setters)

Task: Practice using Getters and Setters to control battery life.

Class Name: Smartphone
Attributes: model, battery_level (default 100).
Methods:
use_app(): Decreases battery by 20.
charge(): Sets battery back to 100.
get_battery(): Returns the current battery level.
Logic Hint (Give if needed): Use the phone multiple times until the battery is low, check the level using the getter, then charge it.w [speed]".

Practice 5: Library Book System (Boolean Logic)

Task: Create a system to manage borrowing books.

Class Name: LibraryBook
Attributes: title, author, is_available (Set to True initially).
Methods:
borrow_book():
If is_available is True: Change it to False and print "You borrowed [title]".
If is_available is False: Print "Sorry, [title] is already borrowed."
return_book(): Set is_available to True.
Logic Hint (Give if needed): Create a book object. Try to borrow it twice in a row (the second time should fail). Then return it and borrow again.
"""
brake(): Decreases speed by 10. Print "Screech! Speed is now [speed]".
Logic Hint (Give if needed): Create a car object. Accelerate 3 times, then brake once.
