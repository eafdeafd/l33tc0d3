'''
The only tricky thing about binary search is the overflow (which doesn't happen in python, but whatever)
What your ending condition is, and what constitutes something you can search through.
In the vanilla case, the ending condition is when both the high and low eventually 
equal each other, you want to run one last time. Either way, low > high by +1 exactly.

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = low + ((high - low) // 2)
        while(low - 1 != high): #Could use low <= high also.
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
            mid = low + ((high - low) // 2)
        return -1