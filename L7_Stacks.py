# https://www.geeksforgeeks.org/stack-data-structure/

#This project showcases the implementation of a stack data 
# structure along with its main operations like push, pop, top, 
# is_empty & size
'''
A Stack is a linear data structure that follows:
LIFO – Last In, First Out
👉 The element inserted last will be removed first.'''
# Methods- top(view top item), 
# push(Insert element on top), 
# pop(Remove top element)
#isEmpty(Check if stack is empty),
#size(Return the number of elements in stack)

# Activity 1: 

#Stack Implementation Using Class
class Stack:
    def __init__(self, n):#contructor to initialize stack and max size
        self.stack = []
        self.n = n #maximum num. of items in the stack (upto user)
    
    '''If current size < maximum size → insert element
        Otherwise → print overflow message'''
    def push(self, k): #k=value to be pushed
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The stack is full.")

    '''If stack is empty → print underflow message
        else → delete the last element and return it'''    
    def pop(self):
        if len(self.stack) == 0: # If the stack is empty then pop should do nothing
            print("The stack is empty.")
        else:
            self.stack.pop(-1) # delete the last element and return it
        return self.stack.pop()#return the popped element
    
    def top(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            return self.stack[-1]#Returns the last element:

    def size(self):
        return len(self.stack)#Returns number of elements. 

    def display(self):
        print(self.stack)#Shows stack content.


s = Stack(3)#stack capacity=3
s.display()
print('\nSize of stack is:', s.size()) 

s.push(5)
s.display()
print('\nSize of stack is:', s.size()) 

s.push(10) 
s.display()
print('\nSize of stack is:', s.size()) 

s.push(15)
s.display()
print('\nSize of stack is:', s.size()) 

s.push(25)
s.display()
print('\nSize of stack is:', s.size()) 

#remove top element
s.pop()
s.display()
print('\nSize of stack is:', s.size()) 
print(s.top(),'\n---------------------------\n')
#---------------------------------------------------

#  Activity 2:

#Given an expression string
#Write a python program to find whether a given string has balanced parentheses or not. 

#One approach to check balanced parentheses is to use stack. 
# Each time, when an open parentheses is encountered push it
#  in the stack, 
# and when closed parenthesis is encountered, 
# match it with the top of stack and pop it. 
# If stack is empty at the end, return Balanced 
# otherwise, Unbalanced. 

open_list = ["[","{","("]
close_list = ["]","}",")"] 

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i) #stack = [{]
        elif i in close_list:
            pos = close_list.index(i) #pos = 1
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced" 
    else:
        return "Unbalanced"


# Driver code
string = "{Hello}"
print(string,"-", check(string))


#--------------------------------------------
"""
Project Description

This project showcases the implementation of a stack data structure along 
with its main operations like push, pop, top, is_empty and size."""



'''
Class Notes:  Stacks

Key Learnings : 
Stacks, applications of stack, and Methods and algorithms with OOPS

Stack:
A stack is a data structure that follows the Last In, First Out (LIFO) principle.
Elements are added and removed from the top of the stack.
Main operations: push (add), pop (remove), top (get top element).
Applications of Stack:
Function call management (call stack)
Undo mechanisms in software
Expression evaluation (e.g., postfix, infix to postfix conversion)
Backtracking algorithms
Memory management (e.g., managing temporary variables)
Methods of a stack data structure:
push(item): Adds an item to the top of the stack.
pop(): Removes and returns the item at the top of the stack.
top(): Returns the item at the top of the stack without removing it.
is_empty(): Returns True if the stack is empty, False otherwise.
size(): Returns the number of items in the stack.
'''
"""
Additional Practice

Practice 1: Reverse a String using a Stack

Task: Create a program that uses a Stack to reverse a user-input string.

Input: "PYTHON"
Goal: Output: "NOHTYP" (LIFO property naturally reverses the order).
Logic(Give if needed):
Create an empty stack (list).
Loop through the string and Push each character onto the stack.
Loop while the stack is not empty: Pop the character and add it to a new result string.
 

Practice 2: The Undo Feature (Simulation)

Task: Simulate a text editor's "Undo" button.

Setup: Create an empty stack history = [] and a string text = "".
Goal: Type "Hello", Type "World" -> Text is "Hello World". Undo -> Text becomes "Hello".
Logic(Give if needed):
"Type": Append a word to text and Push the previous state of text onto the history stack.
"Undo": Pop the last state from history and restore text to that state.
Practice 3: Check for Palindrome using Stack

Task: Use a stack to check if a word is a palindrome (reads the same forwards and backwards).

Input: "racecar"
Goal: "level" -> True, "hello" -> False.
Logic (Give if needed):
Push all characters of the word onto a stack.
Iterate through the original word again.
For each character, pop a character from the stack and compare them.
If all characters match, it is a palindrome.
 

Practice 4: Decimal to Binary Converter

Task: Convert a decimal number to binary using a stack.

Input: 10
Goal: Input 10 -> Output 1010.
Logic (Give if needed):
While number > 0:
Calculate remainder (num % 2).
Push remainder onto the stack.
Divide number by 2 (num // 2).
Pop all elements to form the binary string.
 

Practice 5: Min-Stack (Optimization)

Task: Create a Stack class that can return the minimum element instantly.

Goal: Push [5, 2, 8, 1]. Get Min -> 1. Pop. Get Min -> 2.
Logic (Give if needed):
Maintain two lists: main_stack and min_stack.
Push: Add value to main_stack. If value <= min_stack.top() (or if empty), add to min_stack too.
Pop: Remove from main_stack. If the value was the top of min_stack, remove it from there too.
Get Min: Just return the top of min_stack (O(1) time)."""
