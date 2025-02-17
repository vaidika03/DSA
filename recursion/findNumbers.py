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
