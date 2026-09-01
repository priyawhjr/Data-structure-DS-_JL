

#Practice 2: The "Square Root" Finder 
# (Binary Search Application)

#Task: Use Binary Search logic to find 
# the integer square root of a number without 
# using math.sqrt().
'''
Concept: The square root of x must be between 
0 and x. We can search this range!

Logic  Hint (Give if needed):
Input: x (e.g., 16).
Set low = 0, high = x.
While low <= high:
Calculate mid.
If mid * mid == x: Return mid.
If mid * mid < x: Move low up (mid + 1).
If mid * mid > x: Move high down (mid - 1).
Goal: Find sqrt of 25 (Output: 5) and 10 (Output: 3, integer approximation).
'''

x = int(input("Enter a number: "))

low = 0
high = x
answer = 0   # To store integer square root

while low <= high:
    mid = (low + high) // 2
    
    if mid * mid == x:
        print("Square root is:", mid)
        #print("Square root is:"+ str(mid))
        break
    elif mid * mid < x:
        answer = mid      # Store possible answer
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Square root is:", answer)
    #print("Square root is:"+ str(answer))
