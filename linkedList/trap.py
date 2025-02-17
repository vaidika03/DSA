#17. Trapping Rainwater
def trap(arr):
        n = len(arr)
        left_max = 0
        right_max = 0
        left, right = 0, n - 1
        res = 0
        idx = 0
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    res += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    res += right_max - arr[right]
                right -= 1     
        return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("17. Trapping Rainwater:",trap(height))
