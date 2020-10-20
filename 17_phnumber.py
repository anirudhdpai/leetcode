def pnum(digits):
    l=[[]]
    if not digits or '0' in digits or '1' in digits:
        return []
    dct={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    for i in digits:
        temp=[]
        for r in l:
            for letter in dct[i]:
                temp.append(r+[letter])
        l=temp
    x=[]
    for i in l:
        x.append(''.join(i))
    return x

print(pnum('24'))