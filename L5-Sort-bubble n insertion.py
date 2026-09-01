# Sorting Algo: Bubble sort, Insertion Sort
# https://www.geeksforgeeks.org/bubble-sort/
# https://www.geeksforgeeks.org/insertion-sort/

#Sorting - Rearrange the elements in order
#[3,1,2,5,4] = [1,2,3,4,5] or [5,4,3,2,1]

mylist = [3,1,2,5,4]
print(f'\nOriginal mylist = {mylist}')
mylist.sort(reverse = True)
print(f'Sorted mylist in descending ord. = {mylist}')
print(f'Sorted mylist in acsending ord. : {sorted(mylist, reverse=False)}')
#===================================
# Bubble sort
# Time Complexity - O(n^2)
print('\nBubble Sort')
mylist = [12,34,2,5,7]
print(f'\nOriginal mylist = {mylist}')
for i in range(0, len(mylist)):
  for j in range(i, len(mylist)):
    if mylist[i] < mylist[j]:
        mylist[i],mylist[j] = mylist[j], mylist[i]

print(f'Sorted mylist(Desending) = {mylist}')#Desending order
#-----------------------------

print(f'{"-"*30}\nBubble Sort(Ascending)')

mylist = [12, 34, 2, 5, 7]
print(f'\nOriginal mylist = {mylist}')

for i in range(len(mylist)):
    for j in range(0, len(mylist) - i - 1):
        if mylist[j] > mylist[j + 1]:   # change here for ascending
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print(f'Sorted mylist (Ascending) = {mylist}')


#=======================================
# Insertion Sort
'''1.Divide the list into sorted and unsorted parts.

2.Take one element from the unsorted part and insert 
it into the correct position in the sorted part.'''
# Time Complexity - O(n^2)
print(f'\n{"-"*30} \nInsertion Sort(Ascending):')


mylist = [12, 11, 13, 5, 6]
print(f"\nOriginal mylist = {mylist}")

for i in range(1, len(mylist)):
    key = mylist[i]      # element to insert
    j = i - 1

    # Move elements greater than key one position ahead
    while j >= 0 and mylist[j] > key:
        mylist[j + 1] = mylist[j]
        j -= 1

    mylist[j + 1] = key  # insert at correct position

print(f"Sorted mylist (Ascending) = {mylist}")
#------------------------------
print(f'\n{"-"*30} \nInsertion Sort (Descending):')
print(f"\nOriginal mylist = {mylist}")

for i in range(1, len(mylist)):
    key = mylist[i]      # element to insert
    j = i - 1

    # Move elements greater than key one position ahead
    while j >= 0 and mylist[j] < key:
        mylist[j + 1] = mylist[j]
        j -= 1

    mylist[j + 1] = key  # insert at correct position

print(f"Sorted mylist (Descending) = {mylist}")

"""
Project Description

This project involves the 
implementation of two sort algorithms i.e. bubble sort and insertion sort."""

  # H.W
'''Implement the bubble sort and insertion sort 
to sort the elements in descending order'''

'''
Class Notes:  Sorting Algorithms

Key Learnings : 
Bubble Sort, Insertion Sort
Sorting:
Sorting is the process of arranging elements in a specific order, such as ascending or descending.
It is a fundamental operation in computer science used for organizing and retrieving data efficiently.
Why Sorting?
Sorting helps in organizing data for easier searching, filtering, and analysis.
It is essential for presenting data in a meaningful way, such as in alphabetical or numerical order.
Bubble Sort:
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
Time Complexity: O(n^2) in the worst-case scenario.
Space Complexity: O(1) as it requires only a constant amount of extra space.
Insertion Sort:
Insertion sort builds the final sorted list one element at a time by inserting each element into its correct position.
Time Complexity: O(n^2) in the worst-case scenario.
Space Complexity: O(1) as it requires only a constant amount of extra space.
'''
"""
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
