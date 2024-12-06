# #### **Sorting and Searching**
# 1. Sort an Array Using the Quicksort Algorithm
# 2. Find the Kth Largest and Kth Smallest Number in an Array
# 3. Find the Union and Intersection of Two Sorted Arrays
# 4. Pair with the Given Sum in a Sorted Array
#1. Sort an Array Using the Quicksort Algorithm
#TC: O(nlogn)BEST CASE, O(n^2)WORST CASE , SC :O(logn)
def partition(arr,low,high):
    pivot = arr[high] #5
    i = low-1 #-1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high],arr[i+1]      
    return i+1        
#[1, 7, 8, 9, 10, 5]
def quickSort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
    return arr     

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("quickSort: ",quickSort(arr, 0, n - 1))
#---------------------------------------------------------------
#2. Find the Kth Largest and Kth Smallest Number in an Array
#heapq.heappush
# Time complexity: O(N) BEST CASE , O(N^2) WORST CASE. Space complexity: O(logN)
import heapq
def kth_smallest(arr,k,low,high):
    pi = partition(arr,0,high)
    if pi == k:
        return arr[pi]
    elif pi > k:
        return kth_smallest(arr,k,low,pi-1)
    else :
        return kth_smallest(arr,k,pi+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1
        
"""
#using heap Time Complexity: O(N * log(K)), space Complexity:O(N)
def kth_smallest(arr,k,n):
    heap = []
    for i in range(n):
        heapq.heappush(heap,-arr[i])
        if len(heap)>k:
            heapq.heappop(heap)
    return -heap[0]
"""
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("kth_smallest:",kth_smallest(arr,k-1,0,n-1)) #5
#------------------------------------------
#3. Find the Union and Intersection of Two Sorted Arrays
# TC : O(N) , SC : O(n+m) 
"""
def union_array(a,b):
    a,b = set(a),set(b)
    return list(a | b)

def intersection_array(a,b):
    a,b = set(a),set(b)
    return list(a & b)
"""
def union_array(a,b):
    union = []
    for item in a+b:
        if item not in union:
            union.append(item)
    return union

def intersection_array(a,b):
    intersection = []
    for item in a:
        if item in b and item not in intersection:
            intersection.append(item)
    return intersection       

if __name__ == "__main__":
    a,b = [1, 1, 2, 2, 2, 4],[2, 2, 4, 4]
    print("union_array:",union_array(a,b)) 
    print("intersection_array:",intersection_array(a,b)) 
#---------------------------------------
#4. Pair with the Given Sum in a Sorted Array
def pair_with_given_sum(arr,k):
    setArray = set()
    result = []
    for num in arr:
        rem = k-num
        if rem in setArray:
            result.append((num,rem))
        else:
            setArray.add(num)
    return result       
    
if __name__ == "__main__":
    k = 7
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("pair_with_given_sum:",pair_with_given_sum(arr,k)) 
#------------------------------------------------------------------------
# #### **Subarrays & Prefix Sums**
# 1. Subarray with Given Sum
# 2. Find Whether an Array is a Subset of Another Array
# 3. Subarrays with Equal 1s and 0s
# 4. Find the First Non-Repeating Element in a Given Array of Integers
# 5. Find if There is Any Subarray with a Sum Equal to Zero
# 6. Find the Largest Sum Contiguous Subarray
# 7. Find the Longest Consecutive Subsequence
# 8. Count Pairs with the Given Sum
#------------------------------------------------------------------------
#1. Subarray with Given Sum
#TC: o(N) , SC:O(1)
def subarray_sum(arr, n, target_sum):
    low = 0
    currSum = 0
    for high in range(n):
        currSum += arr[high]
        while currSum > target_sum and low <= high:
            currSum -= arr[low]
            low += 1
        if currSum == target_sum:
            return arr[low:high+1]    
    return 0      
            
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    target_sum = 26
    print(subarray_sum(arr, n, target_sum))
    
#-----------------------------------------------
#2.Find Whether an Array is a Subset of Another Array
# TC: O(N) , SC: O(N)
def check_subset(arr1, arr2):
    arr1 = set(arr1)
    for num in arr2:
        if not num in arr1:
            return False
    return True

if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 8, 1]
    print(check_subset(arr1, arr2))
#---------------------------------------------
#3. Subarrays with Equal 1s and 0s
def countSubarrWithEqualZeroAndOne(arr,n):
    um = {}
    currSum = 0
    for i in range(0,n):
        currSum +=(-1 if (arr[i]==0) else 1)
        um[currSum] = um.get(currSum,0)+1
    count = 0
    for itr in um:
        if um[itr] > 1:
            count += ((um[itr] * int(um[itr] - 1)) / 2)        
    if um.get(0):
        count += um[0]  
    return count        
            
if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 1]
    n = len(arr)
    print("Count =",countSubarrWithEqualZeroAndOne(arr, n))
#---------------------------------------------------------- 
# 4. Find the First Non-Repeating Element in a Given Array of Integers
from collections import defaultdict
def firstNonRepeatingElement(arr,n):
    mp = defaultdict(lambda: 0)
    for i in range(n):
        mp[arr[i]] += 1
    for i in range(n):
        if mp[arr[i]] == 1:
            return arr[i]
    return -1    
        
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 3, 5]
    n = len(arr)
    print("firstNonRepeatingElement =",firstNonRepeatingElement(arr, n))
#----------------------------------------------------------
# 5. Find if There is Any Subarray with a Sum Equal to Zero
def subArrayExists(arr,n):
    nset = set()
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        if currSum == 0 or currSum in nset:
            return True
        nset.add(currSum)
    return False    

if __name__ == "__main__":
    arr = [4, -2, 2, 1, 6]
    n = len(arr)
    print("subArrayExists =",subArrayExists(arr, n))
#----------------------------------------------------------    
# # 6. Find the Largest Sum Contiguous Subarray
def maxSubarraySum(arr,n):
    maxSum = arr[0]
    currSum = arr[0]
    for i in range(1,n):
        currSum = max(currSum +arr[i], arr[i])
        if currSum > maxSum:
            maxSum = currSum
    return maxSum    

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    n = len(arr)
    print("maxSubarraySum =",maxSubarraySum(arr, n))  
    
#-------------------------------------------------------------
#7. Find the Longest Consecutive Subsequence
def findLongestConseqSubseq(arr,n):
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if (arr[i]-1 not in s):
            j = arr[i]
            while(j in s):
                j+=1
            ans = max(ans, j - arr[i])    
    return ans       
if __name__ == "__main__":
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = len(arr)
    print("findLongestConseqSubseq =",findLongestConseqSubseq(arr, n))  
#--------------------------------------------------------------------
#8. count Pairs with the Given Sum in a Sorted Array
def countPairs(arr,k):
    setArray = set()
    result = []
    count = 0
    for num in arr:
        rem = k-num
        if rem in setArray:
            result.append((num,rem))
            count+=1
        else:
            setArray.add(num)
    return count       
    
if __name__ == "__main__":
    k = 7
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("countPairs:",countPairs(arr,k)) 
#--------------------------------------------------------------------------------
#### **Array Manipulation**
# 1. Rearrange the Array in Alternating Positive and Negative Items
# 2. Find the Missing Integer
# 3. Find the Missing And Repeating Element
# 4. Chocolate Distribution Problem
# 5. Find Common Elements in Three Sorted Arrays
#--------------------------------------------------------------------
#1. Rearrange the Array in Alternating Positive and Negative Items
"""
def rearrange(arr):
    pos = []
    neg = []
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    posIdx = 0
    negIdx = 0
    i = 0

    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1

    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1
"""
def rearrange(arr,n):
    pos = 0 
    neg = 1 
    while pos < n and neg < n:
        if arr[pos] >= 0:
            pos += 2
        elif arr[neg] < 0:
            neg += 2
        else:
            arr[pos], arr[neg] = arr[neg], arr[pos]
            pos += 2
            neg += 2
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    n = len(arr)
    print("rearrange:",rearrange(arr,n))
#--------------------------------------------------
#2. Find the Missing Integer
def findMissing(arr,n):
    arrSum = sum(arr)
    expectedSum = n*(n+1)/2
    return expectedSum - arrSum
if __name__ == "__main__":
    arr = [1, 2, 3,5, 6]
    n = len(arr)
    print("findMissing:",findMissing(arr,n+1)) 
#-------------------------------------------------------- 
#3. Find the Missing And Repeating Element
def print_two_elements(arr,n):
    n = len(arr)
    missing = (n * (n + 1)) // 2 
    print("Repeating", end=" ")

    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            missing -= abs(arr[i])  # subtract unique elements
        else:
            print(abs(arr[i]))

    print("Missing", missing)
if __name__ == "__main__":
    arr = [7, 3, 4, 5, 5, 6, 2]
    n = len(arr)
    print_two_elements(arr,n) 
#--------------------------------------------------------------------
#4. Chocolate Distribution Problem
def findMinDiff(arr, m , n):
    arr.sort()  #1,2,3,4,5,6,7
    start = 0
    end = m-1
    minDiff = float('inf')
    currDiff = 0
    while(end < n):
        currDiff = arr[end] - arr[start]
        minDiff = min(minDiff, currDiff)
        start += 1
        end += 1
    return minDiff    
    
if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    print("findMinDiff: ",findMinDiff(arr, m , len(arr)))
    
#-------------------------------------------------------------------
#5. Find Common Elements in Three Sorted Arrays
#for unsorted array
def commonElements(a,b,c):
    intersection1 = []
    for num in a:
        if num in b and num not in intersection1:
            intersection1.append(num)
            
    intersection2 = []        
    for num in intersection1:
        if num in c:
            intersection2.append(num)
        
    return 0 if not intersection2 else intersection2        

"""
#for sorted array
def commonElements(a,b,c):
    i,j,k = 0,0,0
    intersection = []
    while (i<len(a) and j<len(b) and k<len(c)) :
        if a[i] == b[j] and b[j] == c[k]:
            if not intersection or intersection[0] != a[i]:
                intersection.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i] < b[j]:
            i+=1
        elif b[j] < c[k]:
            j+= 1
        else :
            k+= 1
    return intersection
"""
if __name__ == "__main__":
    a = [1, 5, 10, 20, 30]
    b = [5, 13, 15, 200]
    c = [10 ,5]
    print("commonElements:",commonElements(a, b , c))

#-----------------------------------------------------------------------------
    
