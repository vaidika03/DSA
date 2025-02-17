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
