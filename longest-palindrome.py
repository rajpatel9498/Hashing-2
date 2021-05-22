#We would iterate over each character in string. If this character already exists in the set we remove it from the set and add 2 to the length of longest palindrome. If the character dosent exist we simply add it to the set. In the end we return the longest palindrome length.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==0:
            return 0
        res=set()
        count=0
        for i in range(len(s)):
            if s[i] in res:
                res.remove(s[i])
                count = count+2
            else:
                res.add(s[i])
        if len(res)>0:
            count = count +1
        return count
