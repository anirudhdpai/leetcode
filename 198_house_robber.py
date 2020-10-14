def rob(nums):
    n=len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    loot=[0]*(n)
    loot[0]=nums[0]
    loot[1]=max(nums[0],nums[1])
    for i in range(2,n):
        loot[i]=max(loot[i-1],loot[i-2]+nums[i])
    return loot[-1]

print(rob([0]))
print(rob([2,1,1,2]))
print(rob([2,4,6,8]))
