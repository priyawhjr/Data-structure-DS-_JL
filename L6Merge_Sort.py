# Merge  Sort : https://www.geeksforgeeks.org/merge-sort/


# Divide and Conquer Algorithn or merge sort
# Time Complexity - O(nlogn)
'''
print("Merge Sort : ")
def merge(arr, low, mid, high):
  c = []
  start1 = low
  start2 = mid+1

  while start1 <= mid and start2 <=high:
    if arr[start1] < arr[start2]:
      c.append(arr[start1])
      start1 += 1
    else:
      c.append(start2)
      start2 += 1

  while start1 <= mid:
    c.append(arr[start1])
    start1 += 1

  while start2 <= high:
    c.append(arr[start2])
    start2 += 1

  k = 0
  for i in range(low, high+1):
    arr[i] = c[k]
    k += 1

#merge(arr, 0, 2, 5)

def mergeSort(arr, low, high):
  if low < high:
    mid = (low + high) // 2
    mergeSort(arr, low, mid) # 1st partition
    mergeSort(arr, mid+1, high) # 2nd partition
    merge(arr, low, mid, high)  # combining the two paritions in sorted order


arr = [38, 27, 43, 3, 9, 82, 10]
#arr = [12,11,13,5,6,7] #List to be sorted
print(f'Original array = {arr}')
n = len(arr)
mergeSort(arr, 0, n-1)
print(f'\nSorted array using merge sort = {arr}')


Class Notes:  Sorting Algorithms - 2

Key Learnings : 
Merge Sort

Divide and Conquer Strategy:
Problem-solving technique:
Break the problem into smaller parts
Solve parts independently
Combine solutions to solve the original problem
Steps:
Divide: Break problems into smaller, more manageable subproblems.
Conquer: Solve subproblems recursively.
Combine: Combine subproblem solutions to get original problem solutions.

Merge Sort:
Sorting algorithm using divide and conquer:
Divide: Divide the unsorted list into two halves.
Conquer: Recursively sort two halves.
Combine: Merge two sorted halves into a single sorted list.


Merge Strategy:
Merge two sorted arrays into a single sorted array:
Linear time complexity: O(n), n = total elements in arrays.


Merge Sort Time Complexity:
O(n log n), n = number of elements in the array.
Logarithmic due to repeated halving of the array, a linear merge of halves.


Merge Sort Example (Dry Run):
Input array: [38, 27, 43, 3, 9, 82, 10]
Divide:
[38, 27, 43] [3, 9, 82, 10]
[38] [27] [43] [3] [9] [82] [10]
Merge:
[27, 38] [3, 43] [9, 82] [10]
[3, 27, 38, 43] [9, 10, 82]
Final merge:
[3, 9, 10, 27, 38, 43, 82]

'''

#from ast import Add


def merge_sort(arr):
    if len(arr) > 1:#If array has only 1 item → already sorted
        mid = len(arr) // 2 #Divide the Array into 2 halves
        left = arr[:mid]#[start:mid]
        right = arr[mid:]#[mid:end]

        #Recursive Calls to sort both halves
        merge_sort(left)
        merge_sort(right)

        #i=pointer for left, j=pointer for right, 
        # k =pointer for main array
        i = j = k = 0

        #Compare elements at pointers of both subarrays and merge in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:#compare both sides
                arr[k] = left[i]#smaller item goes to main array
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #Add Remaining Elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
print(f'Original array = {arr}')
merge_sort(arr)
print(f'Sorted array using merge sort= {arr}')

"""Project Description
This project includes the implementation of the merge sort algorithm."""
"""Additional Practice

Practice 1: The "Descending" Merge Sort

Task: Modify the standard Merge Sort algorithm to sort numbers from largest to smallest (Descending Order).

Input: [38, 27, 43, 3, 9, 82, 10]
Logic Hint (Give if Needed):
In the merge function, the standard condition is if L[i] < R[j].
Change this condition to if L[i] > R[j] so that larger numbers are placed into the main array first.
Goal: Output should be [82, 43, 38, 27, 10, 9, 3].
Practice 2: Sort Words by Length

Task: Use Merge Sort to arrange a list of words based on their length (shortest first).

Input: ["elephant", "cat", "dog", "hippopotamus", "ant"]
Logic Hint (Give if Needed):
Instead of comparing the string values directly, compare their lengths: len(L[i]) < len(R[j]).
Goal: Output: ['cat', 'dog', 'ant', 'elephant', 'hippopotamus'] (Note: 'cat', 'dog', 'ant' might be in any relative order depending on stability, which is fine).
Practice 3: Merge Two Sorted Lists

Task: Write just the merge function logic (without the full recursion) to combine two already sorted lists into one big sorted list.

Input: List A = [1, 3, 5], List B = [2, 4, 6].
Logic Hint (Give if Needed):
Use two pointers (i for A, j for B).
Compare A[i] vs B[j]. Append the smaller one to a new list C.
Repeat until one list is empty, then add the remaining elements.
Goal: Output: [1, 2, 3, 4, 5, 6].
Practice 4: Count the Steps (Recursion Trace)

Task: Add a print statement inside the mergeSort function to visualize how many times it divides.

Input: [10, 20, 30, 40, 50]
Logic Hint (Give if Needed):
At the start of the mergeSort function, add: print("Splitting:", arr).
At the end (after merging), add: print("Merging:", arr).
Goal: Run the code and observe the output to see the tree structure of the process.
Practice 5: Sort Only Even Numbers

Task: Filter a list to keep only even numbers, then sort them using Merge Sort.

Input: [15, 2, 43, 8, 1, 6, 99]
Logic Hint (Give if Needed):
First, create a new list containing only even numbers: evens = [x for x in arr if x % 2 == 0].
Pass this new list to your mergeSort function.
Goal: Output: [2, 6, 8]."""



