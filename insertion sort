#INSERTION SORT: builds the sorted list one element at a time by repeatedly inserting the next element into its correct position.
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        ele = arr[i]
        idx = i-1
        while(arr[idx] > ele):
            arr[idx+1] = arr[idx]
            idx = idx -1
            if idx < 0:
                break
        arr[idx+1] = ele    
          
if __name__ == "__main__":
    arr = [64, 100, 35, 12, 22, 11, 90]
    insertion_sort(arr)
    print(arr) 
    
# TC: O(N)(BEST CASE) , O(N^2)(WORST CASE)
# stable sorting algo,Adoptive
