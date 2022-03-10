class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        
        if n==1:
            return [-1]
        
        for i in range(n-1):
            arr[i] = max(arr[i+1:])
        
        arr[-1] = -1
        
        return arr

arr = [17,18,5,4,6,1]

sol = Solution()
print(sol.replaceElements(arr))

