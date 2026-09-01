#Project Description:
'''This project showcases the use of the concept of recursion to
 solve problems like the Fibonacci series and the factorial of 
 a number.

'''
# Derive the Fibonacci Formulation through discussion and explanatin
# Fib(n) = Fib(n-1) + Fib(n-2)
"""
The series usually starts with 0 and 1:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34,..."""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci :")
print(fibonacci(3))
print(fibonacci(5))
#-----------------------------------------
"""Examples:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print("\n\nFactorial :")
print(factorial(5))
# print(factorial(8))
#-------------------------------------------
def sumOfNumber(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumber(n-1)

print("\n\nSum of numbers  :")
print(sumOfNumber(3))
# print(sumOfNumber(9))
#----------------------------------------------
def pow(x,y):
  if y == 1:
    return x
  else:
    if y % 2 == 0:
      return (pow(x, y//2) * pow(x, y//2)) 
    else:
      return (y* pow(x, y//2) * pow(x, y//2))


# print(pow(3, 6))
# print(pow(3, 7))
"""
Project Description
This project showcases the use of the concept of recursion to solve 
problems like the Fibonacci series and the factorial of a number."""

""" H.W
Additional Practice

Practice  1: The Rocket Countdown

Task: Create a recursive function that counts down from a number to 0, then prints "Blast off!".

Function Name: countdownNo
Logic  Hint (Give if needed):
Base Case: If n <= 0, print "Blast off!" and return.
Recursive Step: Print n, then return countdown(n - 1).
Goal: Call countdown(5) and see the numbers 5, 4, 3, 2, 1 printed vertically.
Practice  2: Sum of Digits

Task: Calculate the sum of all digits in a number (e.g., 123 -> 1 + 2 + 3 = 6).

Function Name: sum_digitsNo
Logic  Hint (Give if needed):
Base Case: If n == 0, return 0.
Recursive Step: Return (n % 10) + sum_digits(n // 10).
Hint: n % 10 gives the last digit. n // 10 removes the last digit.
Goal: Call sum_digits(456) and print the result (15).
Practice  3: String Reverser

Task: Reverse a string using recursion (without using the [::-1] shortcut).

Function Name: reverse_string(s)
Logic  Hint (Give if needed):
Base Case: If the string is empty (len(s) == 0), return "".
Recursive Step: Return the last character + reverse_string(rest of string).
Code Hint: return s[-1] + reverse_string(s[:-1])
Goal: Input "Python", Output "nohtyP".
Practice  4: List Summation

Task: Find the sum of all numbers in a list using recursion.

Function Name: list_sum(numbers)
Logic  Hint (Give if needed):
Base Case: If the list is empty (len(numbers) == 0), return 0.
Recursive Step: Return numbers[0] + list_sum(numbers[1:]).
Concept: Add the first number to the sum of the rest of the list.
Goal: Pass [10, 20, 30] and get 60.
 

Practice 5: The Palindrome Checker (Challenging)

Task: Check if a word reads the same forwards and backwards (e.g., "racecar", "madam").

Function Name: is_palindrome(word)
Logic  Hint (Give if needed):
Base Case 1: If string length is 0 or 1, return True (it is a palindrome).
Base Case 2: If first char word[0] != last char word[-1], return False.
Recursive Step: Return is_palindrome(word[1:-1]) (Check the middle part of the word).
Goal: Test with "hello" (False) and "level" (True)."""
