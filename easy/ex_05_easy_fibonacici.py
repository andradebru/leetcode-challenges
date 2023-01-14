# https://leetcode.com/problems/fibonacci-number/submissions/877776027/

# just like the previous code, but initiating in zero 
# because its the first number of the fibonacci sequence  

def fib(n: int) -> int:
    first_position = 0
    second_position = 1

    for i in range(n): 
        temp_num = first_position
        first_position = first_position + second_position
        second_position = temp_num
    return first_position

# change number to test other scenarios
print(fib(2))
print(fib(3))
print(fib(4))