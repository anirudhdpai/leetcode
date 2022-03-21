class Solution:
    def restoreString(self, s, indices):
        n = len(s)
        r = [0]*n
        res = ''
        
        for i in range(n):
            r[indices[i]] = s[i]
            
        for i in r:
            res += i
    
        return res

sol = Solution()

s = 'codeleet'
ind = [4,5,6,7,0,2,1,3]
print(sol.restoreString(s,ind))

