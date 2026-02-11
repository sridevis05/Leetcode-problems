class Solution:
    def longestPalindrome(self, s: str) -> int:
        length=0
        for i in s:
            if(s.count(i)>=2):
                length+=2
                s=s.replace(i,"",2)
        if s:
            length+=1
        return length