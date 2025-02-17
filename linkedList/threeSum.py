#16. 3 sum
def threeSum(arr) :
        arr.sort()
        triplets = []
        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate elements
                continue
            l, r = i + 1, len(arr) - 1
            while l < r:
                curr_sum = arr[i] + arr[l] + arr[r]
                if curr_sum == 0:
                    triplets.append([arr[i], arr[l], arr[r]])
                    while l < r and arr[l] == arr[l + 1]:  # Skip duplicate elements for 'l'
                        l += 1
                    while l < r and arr[r] == arr[r - 1]:  # Skip duplicate elements for 'r'
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return triplets
nums = [-1,0,1,2,-1,-4]
print("16. 3 sum:",threeSum(nums))
