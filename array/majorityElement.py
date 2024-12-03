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
