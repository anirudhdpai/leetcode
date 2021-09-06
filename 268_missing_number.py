def missingNumber(self, nums: List[int]) -> int:
    n=len(nums)
    x=n*(n+1)//2
    for i in range(n):
        x-=nums.pop()
    return x

arr = [9,6,4,2,3,5,7,0,1]

print(missingNumber(arr))
