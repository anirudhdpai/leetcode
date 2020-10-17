def find(nums):
    n=len(nums)
    low=0
    high=n-1
    if n==1:
        return nums[0]
    if nums[high]>nums[0]:
        return nums[0]
    while(high>=low):
        mid=low+(high-low)//2
        if nums[mid]>nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1]>nums[mid]:
            return nums[mid]
        if nums[mid]>nums[0]:
            low=mid+1
        else:
            high=mid-1

print(find([0,1,2,3,4,5]))
print(find([2,3,4,5,0,1]))
print(find([3,4,5,0,1,2]))
print(find([4,5,0,1,2,3]))
print(find([5,0,1,2,3,4]))
