def searchMatrix(matrix,target):
    i=0
    j=0
    if not matrix or not matrix[0]:
        return False
    while(i<len(matrix) and j<len(matrix[0])):
        if matrix[i][j]==target:
            return True
        
        try:
            if matrix[i+1][j]<=target:
                i+=1
            else:
                j+=1
        except:
            j+=1
    return False

print(searchMatrix([[1,2,3],[4,5,7]],5))