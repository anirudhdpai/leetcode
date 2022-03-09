def tclose(nums,tar):
    n=len(nums)
    closest=float('inf')
    i=0
    nums.sort()
    for i in range(n-2):
        j=i+1
        k=n-1
        while(j<k):
            s=nums[i]+nums[j]+nums[k]
            if s==tar:
                return s
            if abs(tar-s)<abs(tar-closest):
                closest=s
            if s-tar>0:
                k-=1
            else:
                j+=1
    return closest

arr=[-1,2,1,-4]
print(tclose(arr,1))
            