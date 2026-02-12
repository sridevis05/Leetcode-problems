class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow=0
        con=0
        res=set(s)
        for i in res:
            if i in "aeiou":
                vow=max(vow,s.count(i))
            else:
                con=max(con,s.count(i))
        return vow+con