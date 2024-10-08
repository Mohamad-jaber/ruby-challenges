from typing import List


#function retrun the fibo for the index
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Get user input and validate it
x = int(input("Enter a number: "))

if x < 0:
    print("Please enter a non-negative number.")
else:
    # Print Fibonacci sequence up to the user-specified index
    for n in range(0, x):
        print(fibonacci(n))


# ---------------------------------------------------------------------

#functoin for search miss number and reteun type integer
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for num in nums:
        ans ^= num
    return ans


#ex:
print("-------")
print(missingNumber([1, 3, 2, 0, 5]))
