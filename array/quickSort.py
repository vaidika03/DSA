#1. Sort an Array Using the Quicksort Algorithm
#TC: O(nlogn)BEST CASE, O(n^2)WORST CASE , SC :O(logn)
def partition(arr,low,high):
    pivot = arr[high] #5
    i = low-1 #-1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high],arr[i+1]      
    return i+1        
#[1, 7, 8, 9, 10, 5]
def quickSort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
    return arr     

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("quickSort: ",quickSort(arr, 0, n - 1))
