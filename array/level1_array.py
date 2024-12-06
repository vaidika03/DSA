#sorting
#BUBBLE SORT : placing the first largest element at its correct position. It repeatedly swaps adjacent elements to sort a list..
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print(arr)     
#---------------------------------------------
#INSERTION SORT: builds the sorted list one element at a time by repeatedly inserting the next element into its correct position.
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        ele = arr[i]
        idx = i-1
        while(arr[idx] > ele):
            arr[idx+1] = arr[idx]
            idx = idx -1
            if idx < 0:
                break
        arr[idx+1] = ele    
          
if __name__ == "__main__":
    arr = [64, 100, 35, 12, 22, 11, 90]
    insertion_sort(arr)
    print(arr) 
    
# TC: O(N)(BEST CASE) , O(N^2)(WORST CASE)
# stable sorting algo,Adoptive
#---------------------------------------
#SELECTION SORT: repeatedly selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element.
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_element = arr[i]
        idx = i
        for j in range(i+1,n):
            if(arr[j]< min_element):
                min_element = arr[j]
                idx = j
        arr[idx],arr[i] = arr[i],arr[idx]
if __name__ == "__main__":
    arr = [64, 100, 35, 12, 22, 11, 90]
    selection_sort(arr)
    print(arr)             
     
# TC:O(N^2)(WORST CASE),SC : O(1)
#--------------------------------------
#### **Basic Array Operations**
# 1. Find the Minimum and Maximum Element in an Array
# 2. Array Reverse
# 3. Write a Program to Cyclically Rotate an Array by One
# 4. Sort an Array
# 5. Find the Occurrence of an Integer in the Array
# 6. Find Duplicates in an Array
# 7. Sort the Array of 0s, 1s, and 2s
# 8. Move All the Negative Elements to One Side of the Array
# 9. Find the Row with a Maximum Number of 1’s
# 10. Majority Element
# 11. Wave Array
#--------------------------------------
#1. Find the Minimum and Maximum Element in an Array
#Time Complexity: O(n) , Space Complexity: O(1)
class Pair:
    def __init__(self):
        self.mn = 0  
        self.mx = 0  
      
    # Optimized because it minimizes the number of comparisons
    @staticmethod    
    def getMinMax(arr: list, n: int):
        if n == 0:
            return None
       
        minMax = Pair()
        if n == 1:
            minMax.mn = arr[0]  
            minMax.mx = arr[0]  
            return minMax
        
        if arr[0] > arr[1]:
            minMax.mx = arr[0]  
            minMax.mn = arr[1]  
        else:
            minMax.mx = arr[1]  
            minMax.mn = arr[0]  
        
        for i in range(2, n, 2):
            if i + 1 < n: 
                pair_mn = min(arr[i], arr[i+1])
                pair_mx = max(arr[i], arr[i+1]) 
            else:  
                pair_mn = arr[i]
                pair_mx = arr[i]

            minMax.mn = min(minMax.mn, pair_mn) 
            minMax.mx = max(minMax.mx, pair_mx) 

        return minMax
    
    """
    @staticmethod    
    def getMinMax(arr:list, n :int) :
        minMax = Pair()
        if n ==1 : 
            minMax.mn = arr[0]
            minMax.mx = arr[0]
            return minMax
        
        if arr[0] > arr[1]:
            minMax.mx = arr[0]
            minMax.mn = arr[1]
        else:
            minMax.mx = arr[1]
            minMax.mn = arr[0]

        for i in range(2, n):
            if arr[i] > minMax.mx:
                minMax.mx = arr[i]
            elif arr[i] < minMax.mn:
                minMax.mn = arr[i]

        return minMax
    """
# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = Pair.getMinMax(arr, arr_size)
    print("Minimum element is", minmax.mn) 
    print("Maximum element is", minmax.mx) 

#---------------------------------------
#2Array Reverse using two pointer
# O(n) time with O(1) space complexity.
def reverseArray(arr,n):
    low = 0
    high = n-1
    while (low < high):
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1
    return arr   
    
    
if __name__ == "__main__" :
    arr = [1000, 11, 445, 1, 330, 3000]
    n = len(arr)
    print(reverseArray(arr,n))
#-----------------------------------------------------
# 3. Write a Program to Cyclically Rotate an Array by One
#TC : O(N) , SC : O(1)

#optimixed approach for SC = O(1)
def rotateArray(arr:list,n : int, k : int):
    k = k % n
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr

"""
#SC = O(n)
def rotateArray(arr:list,n : int, k : int):
    output = [0]*n
    idx = 0
    
    for i in range(n-k,n):
        output[idx] = arr[i]
        idx +=1
        
    for i in range(n-k):
        output[idx] = arr[i]
        idx +=1
        
    return output    
"""        
if __name__ == "__main__" :
    arr= [1, 2, 3, 4, 5] 
    n = len(arr)
    k = 2 #rotation degree
    print(rotateArray(arr,n,k))

#------------------------------------------
#5. Find the Occurrence of an Integer in the Array
#use predefined Counter(arr) function
# TC : O(N) , SC : O(1)
def countOccurence(arr,n,element):
    count = 0
    for i in range(n):
        if element == arr[i]:
            count += 1
    return count
"""
def binarySearch(arr, low, high, element, find_first):
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == element:
            result = mid
            # If we want to find the first occurrence, move left
            if find_first:
                high = mid - 1
            # If we want to find the last occurrence, move right
            else:
                low = mid + 1
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return result

def countOccurrence(arr, element,n):
    arr.sort()
    first = binarySearch(arr, 0, n - 1, element, True)
    if first == -1:
        return 0
    last = binarySearch(arr, 0, n - 1, element, False)
    return last - first + 1

#not optimized but can be used if array is already sorted
import bisect
def countOccurrence(arr, element):
    arr.sort()
    first = bisect.bisect_left(arr, element)
    last = bisect.bisect_right(arr, element)
    return last - first
"""
if __name__ == "__main__" :
    arr= [1, 2, 2, 2, 5] 
    n = len(arr)
    element = 2 
    print(countOccurence(arr,n,element))

#-----------------------------------------
#6Find Duplicates in an Array
#TC : O(N) , SC :O(N)
def findDuplicates(arr,n):
    seen = set()
    duplicate = set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        else: 
            seen.add(num)
    return duplicate
"""
from collections import defaultdict
def findDuplicates(arr,n):
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    return [num for num,cnt in count.items() if cnt>1]    
"""
if __name__ == "__main__" :
    arr= [1, 2, 2, 5, 5] 
    n = len(arr)
    print(findDuplicates(arr,n))

#-------------------------------------
#7Sort the Array of 0s, 1s, and 2s.
# TC : O(N) SC: O(N)
def sortColour(arr,n):
    low, mid, high = 0, 0, n - 1 
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1    
    return arr
    
if __name__ == "__main__" :
    arr= [1, 0,2,1,0] 
    n = len(arr)
    print(sortColour(arr,n))
#-----------------------------------
#8Move All the Negative Elements to One Side of the Array
#TC : O(N) , SC:O(N)
"""
def sortNegative(arr,n):
    left,right = 0,n-1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left+=1
        elif arr[left]> 0 and arr[right] < 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[left]> 0 and arr[right] > 0: 
            right -= 1
        else : 
            left += 1
            right -= 1
    return arr       
"""
def sortNegative(arr,n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            arr[j],arr[i] = arr[i],arr[j]
            j = j+1
    return arr                       
if __name__ == "__main__" :
    arr= [-12, 11, -13, -5, 6, -7, 5, -3, -6] 
    n = len(arr)
    print(sortNegative(arr,n))
#--------------------------------------
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
#----------------------------------
#10 Majority element
# Time Complexity: O(n), Space Complexity: O(1)
def majorityElement(arr , n):
    count = 0
    element = 0
    for num in arr:
        if count == 0:
            element = num
        count += (1 if element == num else -1)
    newCount = 0        
    for num in arr:
        if element == num:
            newCount += 1
    if newCount > len(arr) // 2 : 
        return element
    else: 
        None           

if __name__ == "__main__" :
    nums = [2,2,1,1,2,2,2]
    n = len(nums)
    print(majorityElement(nums,n))
    
#----------------------------
#11Wave array 

"""
def waveArray(arr,n):
    arr.sort()
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr    
"""
def waveArray(arr,n):
    for i in range(0,n-1,2):
        if (i >0 and arr[i] > arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
        
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
                        
        
    return arr
if __name__ == "__main__" :
    arr = [1, 10, 12, 6, 3, 2, 20, 100, 80]
    n = len(arr)
    print(waveArray(arr,n))
#-----------------------------------
