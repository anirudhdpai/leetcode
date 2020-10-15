def containsNearbyDuplicate(nums,k):
    n=len(nums)
    dct={}
    for i in range(n):
        if nums[i] in dct:
            if i-dct[nums[i]]<=k:
                return True
            else:
                dct[nums[i]]=i
        else:
            dct[nums[i]]=i
    return False

print(containsNearbyDuplicate([1,2,3,1],3))