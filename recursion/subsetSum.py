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
