#Searching Algo: Lineary, Binary
# https://www.geeksforgeeks.org/binary-search/

#Linear Search Story
'''
Linear Search – The Honest Librarian

Once upon a time, there was a small village library.
The books were placed randomly on a long shelf — no order, no labels.

One day, Priya walks in and says:

“I need the book Python Magic.”

👩‍🏫 The librarian has only one option.

He starts from the very first book.

Book 1 ❌ Not it

Book 2 ❌ Not it

Book 3 ❌ Not it

Book 4 ✅ Found it!

He checks one book at a time, patiently, honestly.

📌 This is Linear Search
Start from the beginning

Check each item one by one

Stop when you find it (or reach the end)
'''


# Linear Search:

'enter the list elements(with space only ,no commas): '
'Ex:1 2 3 4 5'
arr = list(map(int, input("Enter the numbers - ").split()))
#breaks input into pieces.
#map(int,...) → converts each piece into an int.
#list() → stores them in a list
print("Linear Search")
key = int(input('enter item to search: '))

# Method - 1
print('\n method 1:')
if key in arr:
  print(f"Key Exist at index {arr.index(key)}")

# Method - 2
print('\n method 2:')
for i in range(0, len(arr)):
  if arr[i] == key:
    print(f"Key Exist at index {i}")
    break
else:
  print("Key Not Exist")

# Method - 3
print('\n method 3:')
for num in arr:
  if num == key:
    print(f"Key Exist at index {arr.index(num)}")
    break
else:
  print("Key Not Exist")

#Time Complexity of the above Algorithm is O(n).

# Binary Search
# Time Complexity  - O(logn)
# Condition - The array elements should always be sorted

#Binary Search Story
'''Now imagine a big, modern library.

This time, the books are neatly arranged in alphabetical order 📚✨
Again, Lr. asks for Python Magic.
🕵️‍♂️ The detective librarian smiles.
He does not start from the first book.
Instead, he:
Opens the book in the middle
“Is this Python Magic?”
❌ No, this is Java World
He thinks:
“P comes after J… so the book must be on the right side.”

He throws away the left half of the shelf

Opens the middle of the remaining half

✅ Found it!

He keeps cutting the search space in half.

📌 This is Binary Search

Works only on sorted data

Divide the list into halves

Much faster for large data

💡 Life lesson:
When life is organized, smart shortcuts work beautifully.

🧠 Quick Comparison (Story Style)
Linear Search	Binary Search
Searching house-to-house 🚶‍♀️	Using Google Maps 🗺️
Works in any order	Needs sorted order
Slow for big lists	Super fast
Simple & honest	Smart & strategic
🎯 One-Line Memory Trick

Linear Search: “Check everyone, one by one.”

Binary Search: “Cut the problem in half.”

'''
# Method - 1 Recursive
print('\nbinary serch:')

arr = list(map(int, input("Enter the numbers - ").split()))
key = int(input("Enter the item to search: "))
def binary_search(arr, low, high, key):
  
  if low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
      return f'Key Found at index {mid}'
    
    elif arr[mid] < key:
      return binary_search(arr, mid+1, high, key)#using recussive func
    
    else:
      return binary_search(arr, low, mid-1, key)#using recussive func
  
  else:
    return -1
  
result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print(result) #print(f"Key found at index {result}")
else:
    print("Key not found")
  
                   #    arr,   low, high, key)
#print(binary_search([1,2,3,4,5], 0, 4, 9))
#-----------------------------------
print('\n method 2:')
# Method - 2 Iterative
arr = list(map(int, input("Enter the numbers (sorted) - ").split()))
key = int(input("Enter the item to search: "))

start = 0 #start → first index
end = len(arr) - 1#end → last index
'''
If start > end, it means item is not present.'''
while start <= end: #while there are elements to check
    mid = (start + end) // 2# gives middle index.

    if arr[mid] == key:#if middle element is the key, we found it!
        print(f"Key Found at index {mid}")
        break
    elif arr[mid] > key:#if middle element > key, 
        end = mid - 1#then key must be in left half
    else:
        start = mid + 1# if middle element < key, then key must be in right half
else: #The else runs only if loop doesn't break.
    print("No Key Found")

"""Project Description

This project involves the implementation of 
two sort algorithms i.e. bubble sort and insertion sort."""

"""H.W
Additional Practice

Practice 1: The "Descending" Sorter

Task: Modify the standard Bubble Sort algorithm to sort numbers from largest to smallest (Descending Order).

Input: [64, 34, 25, 12, 22, 11, 90]
Logic Hint (Give if needed)
In standard Bubble Sort, we swap if arr[j] > arr[j+1] (pushing large items to the end).
Change the condition to swap if arr[j] < arr[j+1] (pushing small items to the end).
Goal: Output should be [90, 64, 34, 25, 22, 12, 11].
Practice 2: Sort by String Length

Task: Use Insertion Sort to sort a list of words based on their length (shortest word first), not alphabetical order.

Input: ["apple", "kiwi", "banana", "pie", "date"]
Logic Hint (Give if needed):
Use the Insertion Sort structure.
Instead of comparing the strings directly (key < arr[j]), compare their lengths: len(key) < len(arr[j]).
Goal: Output: ['pie', 'kiwi', 'date', 'apple', 'banana'].
Practice 3: The "Almost Sorted" Optimization

Task: Optimize Bubble Sort to stop early if the list is already sorted.

Input: [1, 2, 3, 4, 5] (Already sorted).
Problem: Standard Bubble Sort will still run through all passes ($O(N^2)$), which is wasteful.
Logic Hint (Give if needed):
Create a flag swapped = False at the start of the outer loop.
If a swap happens inside the inner loop, set swapped = True.
If the inner loop finishes and swapped is still False, break the outer loop immediately.
Goal: Add a print statement "Stopped early!" to prove it works on a sorted list.
Practice 4: Sort Last Digit

Task: Sort a list of integers based only on their last digit.

Input: [15, 32, 59, 21, 48]
Logic Hint (Give if needed):
Use Bubble Sort or Insertion Sort.
Comparison logic: Instead of a > b, check (a % 10) > (b % 10).
Goal: The sorted order should be based on [5, 2, 9, 1, 8] -> Result: [21, 32, 15, 48, 59].
Practice 5: The Speed Test (Bubble vs. Insertion)

Task: Compare which algorithm is faster on a semi-random list.

Setup: Create a list of 1000 random numbers. Make a copy so both sort the same data.
Measurement:
Import time.
Record start/end time for Bubble Sort on List A.
Record start/end time for Insertion Sort on List B.
Goal: Print both times. Insertion Sort is generally faster for smaller or partially sorted lists—see if your results confirm this!
"""

