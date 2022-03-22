class Solution:
    def isSameAfterReversals(self, num):
        if num == 0: 
            return True
        if num%10 == 0:
            return False
        else:
            return True

s = Solution()

a = 526
b = 1800
c = 0

print("num, actual, expected")
print(a, s.isSameAfterReversals(a), True)
print(b, s.isSameAfterReversals(b), False)
print(c, s.isSameAfterReversals(c), True)
