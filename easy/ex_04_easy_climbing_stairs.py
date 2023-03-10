# https://leetcode.com/problems/climbing-stairs/submissions/877755040/

# this problem and its solution involves dinamic programming and fibonacci
# in this case we start in 1 because it's the minimum steps required 
# to achieve the top of a stair

def climbStairs(n: int) -> int:
    one = 1
    two = 1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

# change number to test other scenarios
print(climbStairs(3))
print(climbStairs(2))
print(climbStairs(5))
print(climbStairs(10))