#verify if array contains a gray code sequence

def diffByOne(x, y):
    x = "{0:08b}".format(x)
    y = "{0:08b}".format(y)
    diff = 0
    print(x)
    print(y)

    for i in range(len(x)):
        if x[i] != y[i]:
            diff += 1
    
    if diff==1:
        return True
    else:
        return False

def verify_gray_code():
    arr = [0,1,3,2]
    for i in range(len(arr)-1):
        if not diffByOne(arr[i],arr[i+1]):
            return False
    return True
    
print(verify_gray_code())