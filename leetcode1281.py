class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        multi=1
        sum=0
        for i in n:
            multi=multi*int(i)
        for i in n:
            sum=sum+int(i)
        return multi-sum