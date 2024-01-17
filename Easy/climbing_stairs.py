'''
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45


'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # simple dp
        if n <= 2:
            return n
        all_ways_in_one = 1
        all_ways_in_two = 2
        curr = 0
        for i in range(2, n):
            curr = all_ways_in_one + all_ways_in_two
            all_ways_in_one = all_ways_in_two
            all_ways_in_two = curr
        return curr
