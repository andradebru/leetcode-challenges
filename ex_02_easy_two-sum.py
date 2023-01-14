# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in nums:
                if i!=nums.index(second_number):
                    return [i, nums.index(second_number)]
