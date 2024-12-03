#9. Find the Row with a Maximum Number of 1’s
# TC :O(R+C) , SC : O(1)
"""
def findRow(mat,R,C):
    maxRowIdx = 0
    maxSum = 0
    currSum = 0
    for i in range(R):
        currSum = sum(mat[i])
        if(currSum > maxSum):
            maxSum = currSum
            maxRowIdx = i
    return maxRowIdx        
"""         
def findRow(mat,R,C):
    rowIdx = 0
    colIdx = C-1
    maxIdx = 0
    
    while (rowIdx < R and colIdx >=0):
        if mat[rowIdx][colIdx] == 0:
            rowIdx += 1
        else:
            colIdx -= 1
            maxIdx = rowIdx
    return maxIdx        
            

if __name__ == "__main__" :
    mat = [[0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 1, 1, 1, 1]]
    R = len(mat)
    C = len(mat[0])
    print(findRow(mat,R,C))
