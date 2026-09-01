# Class User to explain the concept of hidden attribute 

class User:

    # hidden variable OR private variable
    __password = "Abc@123"
    #To create a private variable or a method, simply put two underscore (__) 
    # before a variable name or a function name as a prefix
            
    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
    
        
    def getPassword(self):
        
        return self.__password # __.variable-> hidden variable
            #Now that we have hidden or made the attributes private, 
            # we still want to get their values. To do this,
            #  we can create a getter function.
            
    def setPassword(self):
        old_password = input("Enter your old password - ")
        if old_password == self.__password:
          new_password = input("Enter your new password - ")
          self.__password = new_password

        else:
          print("Please enter the correct password.\n\n\n") 
          

class Car:
    def __init__(self, brand, model, fuel, color):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.color = color
    
    def getColor(self):
        return self.color
     
    def setColor(self, newColor):
        self.color = newColor
        
    def showCar(self):
        #print("Car - {} - {}, Fuel Type - {}, Color - {}".format(self.brand, self.model, self.fuel, self.color))
        print(f'Car - {self.brand}- {self.model},  fuel Type -{self.fuel}, Color - {self.color} ')
    

# Concept of hidden variable
priya = User("Priya", "priya.jetlearn@gmail.com", "major_priya","xyz@1234")
            #(name, email, username)
# hidden password is not accessible from outside the class
# attribute is accessible from code
print(priya.name)
# hidden password is not accessible
#print(priya.__password) # it will show error. commentout this  line
print(priya.getPassword)
print(priya.getPassword())
priya.setPassword()
#---------------------------------------


class SUV(Car):
    def __init__(self, brand, model, fuel, color, transmission, turbo):
        Car.__init__(self, brand, model, fuel, color)
        self.transmission = transmission
        self.turbo = turbo
        
    def showCar(self):
        #print("Car - {} - {}, Fuel Type - {}, Color - {}, Transmission - {}, Turbo True/False - {}".format(self.brand, self.model, self.fuel, self.color, self.transmission, self.turbo))
        print(f'Car - {self.brand}- {self.model},  Fuel Type -{self.fuel},Color - {self.color}, Transmission - {self.transmission}, Turbo True/False - {self.turbo}')

# Concept of Inheritance
#(self.brand, self.model, self.fuel, self.color, self.transmission, self.turbo)
audiQ3 = SUV("Audi", "Q3", "Disel", "White", "Automatic", True)

# Inherited from class Car
print('\n\n',audiQ3.getColor())
audiQ3.setColor("Red")

# Function overridden in child class is called over here
print(audiQ3.showCar())

#Resourses:
# https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-2-data-hiding-and-object-printing/
# https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/
# https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/
# https://www.geeksforgeeks.org/g-fact-86/?ref=lbp

"""Project Description

This project involves the implementation
of the concept of inheritance by creating parent and child classes."""
#H.W
'''Implementation of Inheritance could be given as homework with 
some examples such as Car -> (sedan, hatchback, SUV).
'''
"""
Additional Practice

Practice 1: The Animal Kingdom (Basic Inheritance)

Task: Create a Parent class and two Child classes to represent animals.

Parent Class: Animal
Attributes: name.
Method: speak() -> Prints "I make a sound".
Child Classes:
Dog(Animal): Method speak() -> Prints "Woof! Woof!".
Cat(Animal): Method speak() -> Prints "Meow! Meow!".
Logic  Hint (Give if needed): Create a dog named "Buddy" and a cat named "Whiskers". Call speak() for both to see how they override the parent method.
Practice 2: The Shape Calculator (Inheritance)

Task: Calculate area using inheritance.

Parent Class: Shape
Method: area() -> Prints "Area not defined".
Child Class: Rectangle(Shape)
Attributes: length, width (in __init__).
Method: area() -> Returns length * width.
Child Class: Circle(Shape)
Attributes: radius.
Method: area() -> Returns 3.14 * radius * radius.
Logic  Hint (Give if needed): Create a Rectangle (10, 5) and a Circle (7). Print their areas.
Practice 3: Employee System (Using super())

Task: Use super() to extend a parent class constructor.

Parent Class: Employee
Attributes: name, id.
Method: show_details().
Child Class: Manager(Employee)
Attributes: Add department (e.g., "HR", "Sales").
Logic  Hint (Give if needed): In __init__, use super().__init__(name, id) to handle the basic setup, then set self.department = department.
Override show_details() to include the department.
Practice 4: The Vehicle Showroom (Multi-Level Inheritance)

Task: Create a chain of inheritance.

Parent: Vehicle (Attribute: brand).
Child: Bike(Vehicle) (Attribute: type e.g., "Sport", "Cruiser").
Grand-Child: ElectricBike(Bike) (Attribute: battery_capacity).
Logic  Hint (Give if needed): Create an ElectricBike object. It should have access to brand, type, AND battery_capacity. Print all three.
Practice 5: Algorithm Race (Time Complexity Concept)

Task: Compare two ways to solve a problem (Simulating Time Complexity).

Goal: Sum numbers from 1 to N.
Method A (Loop): Use a for loop to add numbers. (O(N) - Linear Time).
Method B (Formula): Use the math formula n * (n + 1) / 2. (O(1) - Constant Time).
Logic  Hint (Give if needed): Write both functions. Pass N = 100 to both and print the results to prove they give the same answer.
"""
