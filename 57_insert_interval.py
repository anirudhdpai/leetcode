def insert(intervals,newInterval):
    intervals.append(newInterval)
    res=[]
    intervals.sort()
    for i in intervals:
        if res and res[-1][-1]>i[0]:
            res[-1][-1]=max(res[-1][-1],i[-1])
        else:
            res.append(i)
    return res



print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(insert([[1,3],[6,9]],[2,5]))
print(insert([[10,15]],[16,17]))
print(insert([[1,10]],[2,8]))