'''
nifty algorithm
169. Majority Element
Solved
Easy
Topics
Companies

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # linear time linear space is trivial, use hashmap
        # linear time constant space seems harder. 
        # do i need to use some median, mean, trick here?
        # moore voting algorithm
        count = 0
        candidate = 'abc'
        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            elif candidate == i:
                count += 1
            else:
                count -= 1
        return candidate
