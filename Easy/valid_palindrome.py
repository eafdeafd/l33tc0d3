'''
Notes: I wonder if there is a better way to do this.
For some reason I feel nitpicky in time complexity for these leetcodes, but
its 2n time when I think a single two pointer solution could work, just more thinking needed.


A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.


'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        front = 0
        end = len(s) - 1
        if len(s) == 0:
            return True
        while front < end:
            if s[front]!= s[end]:
                return False
            front += 1
            end -= 1
        return True