
'''Linear Search Algorithm
Linear search is a simple search algorithm that checks each 
element in a list sequentially until the desired'''

#arr=list of items, key= item to search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i      # key found at index i
    return -1             # key not found

arr = list(map(int, 
               input("Enter list items(with space only ,no commas ): ").split()))
key = int(input("Enter the item to search: "))

result = linear_search(arr, key)#arr=list of items, key= item to search

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
"""
Project Description
This project involves the implementation of linear and binary search algorithms."""
"""H.W.
Additional Practice

Practice 1: The "Contact Finder" (Linear Search)

Task: Create a program that searches for a specific name in a list of contacts.

Input: Create a list contacts = ["Alice", "Bob", "Charlie", "David", "Eve"].
User Input: Ask the user "Who are you looking for?".
Logic (Linear) Hint (Give if needed):
Loop through the list from start to end.
If contacts[i] == user_input, print "Found [Name] at index [i]".
If the loop finishes without finding it, print "Contact not found".
Practice 2: The "Square Root" Finder (Binary Search Application)

Task: Use Binary Search logic to find the integer square root of a number without using math.sqrt().

Concept: The square root of x must be between 0 and x. We can search this range!
Logic  Hint (Give if needed):
Input: x (e.g., 16).
Set low = 0, high = x.
While low <= high:
Calculate mid.
If mid * mid == x: Return mid.
If mid * mid < x: Move low up (mid + 1).
If mid * mid > x: Move high down (mid - 1).
Goal: Find sqrt of 25 (Output: 5) and 10 (Output: 3, integer approximation).
Practice 3: Search Insert Position (Binary Search Variant)

Task: Given a sorted array and a target value, return the index where the target would be if it were inserted in order.

Input: Sorted List [1, 3, 5, 6], Target 5. -> Output: 2.
Input: Sorted List [1, 3, 5, 6], Target 2. -> Output: 1 (It belongs between 1 and 3).
Logic  Hint (Give if needed):
Perform a standard Binary Search.
If found, return the index.
If not found, return the low pointer (this is usually where the element belongs).
Practice 4: The Smallest Missing Number

Task: Given a sorted array of distinct non-negative integers (starting from 0), find the smallest missing number.

Input: [0, 1, 2, 4, 5, 6] (Missing 3).
Logic  Hint (Give if needed):
In a perfect array, arr[index] should equal index (e.g., index 0 has 0, index 1 has 1).
Use Binary Search.
If arr[mid] == mid: The missing element is in the right half (indices match so far).
If arr[mid] != mid: The missing element is in the left half (mismatch happened earlier).
Practice 5: The Speed Race (Time Complexity Demo)

Task: Prove that Binary Search is faster than Linear Search.

Setup: Create a huge sorted list: numbers = list(range(1, 1000001)) (1 million numbers).
Target: Search for the last number (1000000).
Measurement:
Import time module.
Record start_time, run Linear Search, record end_time. Print duration.
Record start_time, run Binary Search, record end_time. Print duration.
Observation: Notice how Linear search takes milliseconds/seconds, while Binary is almost instant (0.0 seconds).
"""
