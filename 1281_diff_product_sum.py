def subtractProductAndSum(n):
    digs=[int(i) for i in str(n)]
    res=1
    for i in digs:
        res*=i
    for i in digs:
        res-=i
    return res

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))
print(subtractProductAndSum(12))