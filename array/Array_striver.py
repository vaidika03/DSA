#1 Set Matrix Zeros
def setZeroes(matrix):
    m,n = len(matrix),len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(n))
    first_col = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    if first_row:
        for j in range(1,n):
            matrix[0][j] = 0
            
    if first_col:
        for i in range(1,m):
            matrix[i][0] = 0
    return matrix        
            
if __name__ =="__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("setZeroes:",setZeroes(matrix))
#------------------------------------------------------------------------------    
#2 Pascal's Triangle
def printPascal(n):
    triangle = []     
    for row in range(1, n + 1):
        row_values = []  
        c = 1
        for i in range(1, row + 1):
            row_values.append(c) 
            c = c * (row - i) // i 
        triangle.append(row_values) 
    return triangle
if __name__ == "__main__":
    n = 5
    print("printPascal",printPascal(n))
#---------------------------------------------------------------------------------------
#3 Next Permutation
def next_permutation(arr):
    n = len(arr)    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break 
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return
    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
    # Reverse the elements from pivot + 1 to the end in place
    arr[pivot+1:] = arr[pivot+1:][::-1]

arr = [ 2, 4, 1, 7, 5, 0 ]
next_permutation(arr)
print("next permutation:"," ".join(map(str, arr)))
#----------------------------------------------------------------------------
#4 Kadane's Algorithm
def maxSubarraySum(arr):    
    res = arr[0]
    maxSum = arr[0]
    for i in range(1, len(arr)):
        maxSum = max(maxSum + arr[i], arr[i])
        res = max(res, maxSum)   
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print("maxSubarraySum",maxSubarraySum(arr))
#--------------------------------------------------------------------------
#5 Function to sort an array of 0s, 1s and 2s
def sort012(arr):
    n = len(arr)
    lo = 0
    hi = n - 1
    mid = 0

    # Iterate till all the elements are sorted
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
        
    return arr
arr = [0, 1, 2, 0, 1, 2]
arr = sort012(arr)
print("sort array of 0,1,2:",arr)

#--------------------------------------------------------------------------
#6 Stock Buy and Sell
def buyAndSell(arr):
    n = len(arr)
    profit = 0
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            profit += arr[i]-arr[i-1]
    return profit

arr = [100, 180, 260, 310, 40, 535, 695] 
print("buyAndSell",buyAndSell(arr))   
#--------------------------------------------------------------------------------------
#7 Rotate Matrix
def rotateMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n): 
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i].reverse()    
    return mat
"""
def rotateMatrix(mat):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] =  mat[j][n-i-1]
    return res
    
"""
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("rotateMatrix:",rotateMatrix(mat))


#----------------------------------------------------------------------------------------
#8 Find the duplicate in an array of N+1 integers
def findDuplicate1(arr):
    n = len(arr)
    res=[]
    for i in range(n):
        num = abs(arr[i])
        if arr[num]< 0:
            res.append(num)
        else:
            arr[num] = -arr[num]
    return res    

arr=[1, 2, 3, 6, 3, 6, 1]    
print("findDuplicate",findDuplicate1(arr))   
#------------------------------------------------------------------------------
#9 Repeat and Missing Number
def findDuplicate(arr):
    n = len(arr)
    res=[]
    missing = n*(n+1)//2
    for i in range(n):
        num = abs(arr[i])
        if arr[num-1]< 0:
            duplicate = num
        else:
            arr[num-1] = -arr[num-1]
            missing -= num
    str1 = f"missing: {missing}, duplicate: {duplicate}" 
    return  str1

arr=[4, 3, 5, 2, 2, 1]    
print("findDuplicate",findDuplicate(arr))
#------------------------------------------------------------------------------
#10 Majority Element (>n/2 times)
def majorityElement(arr):
    n = len(arr)
    count = 1
    num = arr[0]
    for i in range(1,n):
        if count <= 0:
            num = arr[i]
        if arr[i] == num:
            count+=1
        else:
            count-=1    
    return(num)

arr = [1, 1, 2, 2, 2, 5, 1]
print("majorityElement",majorityElement(arr))
#----------------------------------------------------------------------------------
#11 2Sum Problem
def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

nums = [2,7,11,15]
target = 9
print("twoSum",twoSum(nums, target))
#-------------------------------------------------------------------------------------
#12 4-Sum Problem

def fourSum( arr, target):
    res = []
    n = len(arr)
    arr.sort()  # Sort the array first
    for i in range(n - 3):  # The first number in the quadruplet
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicates for i
            continue
        for j in range(i + 1, n - 2):  # The second number in the quadruplet
            if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicates for j
                continue
            left, right = j + 1, n - 1  # Two pointers for the remaining two numbers
            while left < right:
                currSum = arr[i] + arr[j] + arr[left] + arr[right]
                if currSum == target:
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    # Skip duplicates for left and right
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif currSum < target:
                    left += 1  # Move the left pointer right to increase the sum
                else:
                    right -= 1  # Move the right pointer left to decrease the sum
    return res
arr = [1,0,-1,0,-2,2]
target = 0
print("fourSum",fourSum(arr, target))
#----------------------------------------------------------------------------------------------
#13 Longest Consecutive Sequence
def longestConsecutive(arr):
    n = len(arr)
    clean = sorted(set(arr))
    count = 1
    maxLen = 0
    last = None
    for x in clean:
        if x-1 == last:
            count += 1
        else:
            if count > maxLen:
                maxLen=count
            count = 1
        last = x
    if count > maxLen:
        maxLen = count
    return maxLen
arr = [1, 9, 3, 10, 4, 20, 2]
print("longestConsecutive",longestConsecutive(arr))
#----------------------------------------------------------------------------------------------
#14 Largest Subarray with K sum
"""
def lenOfLongSubarr(arr, k):
    res = 0
    for i in range(len(arr)):
        # Sum of subarray from i to j
        total_sum = 0
        for j in range(i, len(arr)):
            total_sum += arr[j]
            if total_sum == k:
                res = max(res, j - i + 1)
    return res
"""
def lenOfLongSubarr(arr, k):
    sum_map = {0: -1}  
    total_sum = 0
    max_length = 0
    for i in range(len(arr)):
        total_sum += arr[i]
        if total_sum - k in sum_map:
            max_length = max(max_length, i - sum_map[total_sum - k])
        if total_sum not in sum_map:
            sum_map[total_sum] = i
    return max_length
arr = [10, 5, 2, 7, 1, 9]
arr = [1,2,1,2,1]
k = 3
print("lenOfLongSubarr",lenOfLongSubarr(arr, k))
#-----------------------------------------------------------------------------
#15 Longest Substring without repeat
def longestUniqueSubstr(s):
    n = len(s)
    res = 0
    last_index = [-1]* 256
    start = 0
    for end in range(n):
        start = max(start,last_index[ord(s[end])]+1)
        res = max(res,end-start+1)
        last_index[ord(s[end])] = end
    return res

s = "geeksforgeeks"
print("longestUniqueSubstr",longestUniqueSubstr(s))
#-----------------------------------------------------------------------------
#16 Majority Element (n/3 times)
"""
def findMajority(arr):
    n = len(arr)
    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0
    for ele in arr:
        if ele == ele1:
            cnt1+=1
        elif ele == ele2:
            cnt2+=1
        elif cnt1 == 0:
            ele1 = ele
            cnt1+=1
        elif cnt2 == 0:
            ele2 = ele
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    res = []
    cnt1, cnt2 = 0, 0
    for ele in arr:
        if ele1 == ele:
            cnt1+=1
        if ele2 == ele:
            cnt2 += 1
            
    if cnt1 > n / 3:
        res.append(ele1)
    if cnt2 > n / 3 and ele1 != ele2:
        res.append(ele2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res
"""
from collections import Counter
def findMajority(arr):
        x = []
        y = Counter(arr)
        for i in y:
            if y[i]>len(arr)//3:
                x.append(i)
        return x

arr = [2, 2, 3, 1, 3, 2, 1, 1]
arr =  [3,2,3]
print("findMajority:",findMajority(arr))
#-----------------------------------------------------------------------------
#17 Grid Unique Paths
"""
def number_of_paths(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m+1):
        dp[i][0] = 1
    for j in range(n+1):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]
"""
def number_of_paths(m, n):
    dp = [1]*(m)
    for i in range(n-1):
        for j in range(1,m):
            dp[j] += dp[j-1]
    return dp[m-1]

n, m = 3, 3
print("number_of_paths:",number_of_paths(m, n))
#---------------------------------------------------------------------------
#18 Merge two sorted arrays without extra space
def mergeArrays(a, b):
    n,m = len(a),len(b)
    i,j = n-1,0
    while i>=0 and j<m:
        if a[i] > b[j]:
            a[i],b[j] = b[j],a[i]
            i-=1
            j+=1
        else:
            i-=1
    a.sort()
    b.sort()
    print(a,b)

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
print("mergeArrays:")
mergeArrays(a, b)
#----------------------------------------------------------------------
#19 Search in a 2 D matrix
def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
    i,j = 0,m-1
    while i<n and j>=0:
        if x>mat[i][j]:
            i+=1
        elif x<mat[i][j]:
            j-=1
        else:
            return True
    return False
            
mat =[
    [3, 30, 38],
    [20, 52, 54],
    [35, 60, 69]
]
x = 35
print("matSearch:",matSearch(mat, x))
#----------------------------------------------------------------------------------
#20 Pow(x, n)
"""
def power(x, y):
    temp = 0
    if(y == 0):
        return 1
    if y < 0:
        return 1 / power(x, -y)
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        return x * temp * temp
"""
def power(x, y):    
    return x**n
x = 2
y = 3
print(f"power({x}^{y}):",power(x, y))
