#6Move All the Negative Elements to One Side of the Array
#TC : O(N) , SC:O(N)
"""
def sortNegative(arr,n):
    left,right = 0,n-1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left+=1
        elif arr[left]> 0 and arr[right] < 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[left]> 0 and arr[right] > 0: 
            right -= 1
        else : 
            left += 1
            right -= 1
    return arr       
"""
def sortNegative(arr,n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            arr[j],arr[i] = arr[i],arr[j]
            j = j+1
    return arr                       
if __name__ == "__main__" :
    arr= [-12, 11, -13, -5, 6, -7, 5, -3, -6] 
    n = len(arr)
    print(sortNegative(arr,n))

---------------------------------
