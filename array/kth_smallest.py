#2. Find the Kth Largest and Kth Smallest Number in an Array
#heapq.heappush
# Time complexity: O(N) BEST CASE , O(N^2) WORST CASE. Space complexity: O(logN)
import heapq
def kth_smallest(arr,k,low,high):
    pi = partition(arr,0,high)
    if pi == k:
        return arr[pi]
    elif pi > k:
        return kth_smallest(arr,k,low,pi-1)
    else :
        return kth_smallest(arr,k,pi+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1
        
"""
#using heap Time Complexity: O(N * log(K)), space Complexity:O(N)
def kth_smallest(arr,k,n):
    heap = []
    for i in range(n):
        heapq.heappush(heap,-arr[i])
        if len(heap)>k:
            heapq.heappop(heap)
    return -heap[0]
"""
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("kth_smallest:",kth_smallest(arr,k-1,0,n-1)) #5
