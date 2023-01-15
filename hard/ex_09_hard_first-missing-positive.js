// # https://leetcode.com/problems/first-missing-positive/

// /**
//  * @param {number[]} nums
//  * @return {number}
//  */

var firstMissingPositive = function (nums) {
  let numsMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    numsMap.set(nums[i], 1);
  }
  for (let i = 1; i <= nums.length; i++) {
    if (!numsMap.has(i)) {
      return i;
    }
  }
  return nums.length + 1;
};

// change the array to test other scenarios
console.log(firstMissingPositive([1, 2, 0]));
console.log(firstMissingPositive([3, 4, -1, 1]));
