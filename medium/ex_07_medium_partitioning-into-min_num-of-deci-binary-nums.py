# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

# class Solution:
def minPartitions(n: str) -> int:
    max_num = 0
    for character in n:
        max_num = max(max_num, ord(character)-ord('0'))
        # The ord() function returns an integer representing the Unicode character.

    return max_num

print(minPartitions('32'))
print(minPartitions('82734'))
print(minPartitions('27346209830709182346'))
