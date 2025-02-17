#14. Remove Duplicate from Sorted array
def removeDuplicates(nums):
    k = 1
    res = []
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return nums[:k]

nums = [1,1,2]
print("14. Remove duplicates inplace:",removeDuplicates(nums))
