class Solution:
    def judgeCircle(self, moves: str) -> bool:
        org = [0,0]
        for i in moves:
            if i == "U":
                org[0] += 1
            elif i == "D":
                org[0] -= 1
            elif i == "L":
                org[1] -= 1
            elif i == "R":
                org[1] += 1
        if org[0]==0 and org[1]==0:
            return True
        return False

s = Solution()

moves = 'UD'
print(s.judgeCircle(moves))
moves = 'RLUDDULRR'
print(s.judgeCircle(moves))
moves = 'UDLDURUDRL'
print(s.judgeCircle(moves))
