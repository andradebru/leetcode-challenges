# https://leetcode.com/problems/permutation-sequence/

# class Solution:
import math


def getPermutation(n: int, k: int) -> str:
    while n > 0:
        nums = [str(i) for i in range(1, n+1)]
        kth_permutation = [] # permutation 'number k'
        factorial = math.factorial(n)
        index = k-1

        while nums:
            factorial = factorial // len(nums)
            position = index // factorial
            number = nums.pop(position)
            kth_permutation.append(number)
            index = index % factorial

        return "".join(kth_permutation)

# change the numbers to test other scenarios
print(getPermutation(3, 3))
print(getPermutation(4, 9))
print(getPermutation(3, 1))
