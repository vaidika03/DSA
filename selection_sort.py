#SELECTION SORT: repeatedly selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element.
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_element = arr[i]
        idx = i
        for j in range(i+1,n):
            if(arr[j]< min_element):
                min_element = arr[j]
                idx = j
        arr[idx],arr[i] = arr[i],arr[idx]
if __name__ == "__main__":
    arr = [64, 100, 35, 12, 22, 11, 90]
    selection_sort(arr)
    print(arr)             
     
# TC:O(N^2)(WORST CASE),SC : O(1)
