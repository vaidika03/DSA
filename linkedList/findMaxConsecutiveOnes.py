#15. Max consecutive ones
def findMaxConsecutiveOnes(nums):
    maxi = count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > maxi:
                maxi = count
            count = 0
    return max(maxi, count)

nums = [1,1,0,1,1,1]
print("15. findMaxConsecutiveOnes:",findMaxConsecutiveOnes(nums))
