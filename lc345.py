class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        v=[i for i in s if i in vowels]
        res=""
        for i in s:
            if i in vowels:
                res+=v.pop()
            else:
                res+=i
        return res        