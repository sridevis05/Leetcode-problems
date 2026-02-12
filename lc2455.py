class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            if(i%3==0 and i%2==0):
                sum+=i
        return sum//2