class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        if n==0:
            return arr
        i = 0
        j = 1
        count = 1
        while(i<n-1):
            if arr[i]==arr[i-1]:
                count-=2
                break
            while(arr[j]==arr[i] and j<n-1):
                j+=1
            i+=1
            count+=1
            arr[i]=arr[j]
            if j==n-1:
                break
    
        return count,arr


arr = [1,1,1,1,2,2,2,2,3,3,4,4]
ar = [1,2]

a = Solution()
x,y = a.removeDuplicates(arr)
print(x)
print(arr)
print(arr[:x])
