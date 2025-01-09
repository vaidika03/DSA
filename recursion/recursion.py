#Recursion
#1. generate all subset.
#2. Subset Sums
#3. SubsetII(Generate_subsets without duplicates)
#4. Combination sum-1
#5. Combination sum-2
#6. Palindrome Partitioning
#--------------------------------------------------------------------------------------
#1. generate all subset.
def generate_subsets(nums, idx, currSubset, res1):
    if idx == len(nums):
        res1.append(list(currSubset))
        return
    generate_subsets(nums, idx+1, currSubset, res1)
    
    currSubset.append(nums[idx])
    generate_subsets(nums, idx+1, currSubset, res1)
    
    currSubset.pop()    
def subsets(nums):
    res1 = []
    generate_subsets(nums, 0, [], res1)
    return res1
nums = [1, 2, 1]
print("1. Generate_subsets:",subsets(nums))


#------------------------------------------------------------------
"""
subsetSum = []
for subset in subsets(nums):
    subsetSum.append(sum(subset))
    
print("2.SubsetSum: ",subsetSum)
"""
def subsetSum(nums, idx, currSubset, res2):
    if idx == len(nums):
        res2.append(sum(currSubset))
        return
    subsetSum(nums, idx+1, currSubset, res2)
    
    currSubset.append(nums[idx])
    subsetSum(nums, idx+1, currSubset, res2)
    
    currSubset.pop()    
def subsets(nums):
    res2 = []
    subsetSum(nums, 0, [], res2)
    return res2

nums = [1, 2, 1]
print("2. subsetSum:",subsets(nums))
#-----------------------------------------------------------
#3. SubsetII(Generate_subsets without duplicates)
def generate_subsets2(nums, idx, currSubset, result):
    if idx == len(nums):
        currSubset.sort()
        result.add(tuple(currSubset))
        return
    generate_subsets2(nums, idx+1, currSubset, result)
    
    currSubset.append(nums[idx])
    generate_subsets2(nums, idx+1, currSubset, result)
    
    currSubset.pop()    
def subsetsII(nums):
    nums.sort()
    result = set()
    generate_subsets2(nums, 0, [], result)
    res = [list(tup) for tup in result]
    res.sort()
    return res
nums = [4,1,0]
print("3. SubsetII(Generate_subsets without duplicates):",subsetsII(nums))
#--------------------------------------------------------------------------------------
#Combination sum-1
def findNumbers(ans, arr, currSet, Sum, idx):    
    if Sum == 0:
        ans.append(list(currSet))
        return
    
    for i in range(idx,len(arr)):
        if (Sum - arr[i])>=0:
            currSet.append(arr[i])
            findNumbers(ans, arr, currSet, Sum-arr[i], i)
            currSet.remove(arr[i])

def combinationSumI(arr, Sum):
    ans = []
    currSet = []
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, currSet, Sum, 0)
    return ans
    
arr = [2,3,6,7]
target = 7
print("4. combinationSumI:",combinationSumI(arr, target))
#----------------------------------------------------------------------------------
def findNumbersII(ans, arr, currSet, Sum, idx):    
    if Sum == 0:
        ans.append(list(currSet))
        return
    
    for i in range(idx,len(arr)):
        if i > idx and arr[i] == arr[i - 1]:
            continue
            
        if arr[i]>Sum:
            break
        currSet.append(arr[i])
        findNumbersII(ans, arr, currSet, Sum-arr[i], i+1)
        currSet.remove(arr[i])

def combinationSumII(arr, Sum):
    ans = []
    currSet = []
    arr.sort()
    findNumbersII(ans, arr, currSet, Sum, 0)
    res = [list(tup) for tup in ans]
    res.sort()
    return res
    
arr = [10,1,2,7,6,1,5]
target = 8
#arr = [1]*100, target = 30
print("5. combinationSumII:",combinationSumII(arr,target))
#---------------------------------------------------------------------------
#6. Palindrome partitioning of string.
def isPalindrome(s):
    return s == s[::-1]
def findSet(s,ans,currSet,idx):
    if idx >= len(s):
        ans.append(list(currSet))
        return
    
    for i in range(idx+1,len(s)+1):
        substr = s[idx:i]
        if isPalidrome(substr):
            currSet.append(substr)
            findSet(s,ans,currSet,i) 
            currSet.pop()
                
def palPartitionRec(s):
    ans = []
    currSet = []
    res = ""
    findSet(s,ans,currSet,0)
    return ans

s = "aab"
print("6. palPartitionRec:",palPartitionRec(s))
#---------------------------OUTPUT-----------------------------------------------------------
# 1. Generate_subsets: [[], [1], [2], [2, 1], [1], [1, 1], [1, 2], [1, 2, 1]]
# 2. subsetSum: [0, 1, 2, 3, 1, 2, 3, 4]
# 3. SubsetII(Generate_subsets without duplicates): [[], [0], [0, 1], [0, 1, 4], [0, 4], [1], [1, 4], [4]]
# 4. combinationSumI: [[2, 2, 3], [7]]
# 5. combinationSumII: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# 6. palPartitionRec: [['a', 'a', 'b'], ['aa', 'b']]
