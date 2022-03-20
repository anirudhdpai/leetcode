class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        n = len(nums)
        size = 1
        prev = nums[0]
        ind = 1
        for i in range(1,n):
            if nums[i] != prev:
                size += 1
                prev = nums[i]
                nums[ind]=nums[i]
                ind+=1
        return size

s = Solution()
nums = [1,1,2,2,2,2,3,3,3,4,4]

print(s.removeDuplicates(nums),nums)
