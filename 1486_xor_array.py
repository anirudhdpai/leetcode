def xor_of_array(n, start):
    res = start
    num = start
    for i in range(1,n):
        num = num + 2
        res = res^num
    return res

def main():
    print(xor_of_array(5,1))

main()