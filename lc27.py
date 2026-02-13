class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[]
        for i in range(0,len(nums)):
            if nums[i]!=val:
                res.append(nums[i])
        for i in range(0,len(res)):
            nums[i]=res[i]
        return len(res)