from collections import Counter
class Solution:
    def minDominoRotations(self, A, B):
        x=len(A)
        freqa=Counter(A)
        freqb=Counter(B)
        mxc=0
        num=-1
        
        flag=0
        for i in freqa:
            if freqa[i]>mxc:
                num=i
                mxc=freqa[i]
        for i in freqb:
            if freqb[i]>mxc:
                num=i
                mxc=freqb[i]
                flag=1
        form=B if flag else A
        other=A if flag else B
        count=0
        for i in range(x):
            if form[i]!=num:
                if other[i]==num:
                    count+=1
                else:
                    return -1
        return count
                    