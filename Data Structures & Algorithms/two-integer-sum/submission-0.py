class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        
l=Solution()
print(l.twoSum([1,2,3,4,6],5))