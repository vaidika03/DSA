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

