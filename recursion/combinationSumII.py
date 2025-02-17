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
