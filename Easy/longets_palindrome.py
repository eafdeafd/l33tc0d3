'''
409. Longest Palindrome
Solved
Easy
Topics
Companies

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

 

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.


'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)
        palindrome_length = 0
        found_middle = False
        for count in char_counts.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                found_middle = True

        return palindrome_length + (1 if found_middle else 0)
