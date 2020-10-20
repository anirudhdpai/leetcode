def tsum(nums):
    n=len(nums)
    i=0
    l=[]
    nums.sort()
    while(i<n):
        j=i+1
        k=n-1
        while(j<k):
            tri=nums[i]+nums[j]+nums[k]
            if tri==0:
                l.append([nums[i],nums[j],nums[k]])
                j+=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
                k-=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1
            elif tri>0:
                k-=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1
            else:
                j+=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
        i+=1
        while(i<n and nums[i]==nums[i-1]):
            i+=1
    return l

arr=[-1,0,1,2,-1,-4,4]
print(tsum(arr))