#Counting sort sorts by counting element frequencies and using counts to place elements in order.
def counting_sort(arr):
    #find max of input arr
    n = len(arr)
    maxval = max(arr)     
    #create array with size max+1
    count_array = [0]*(maxval+1)
    #freq of each element in count_array
    for num in arr:
        count_array[num] += 1
    #prefix sum
    for i in range(1,maxval+1):
        count_array[i] += count_array[i-1]
    output_array = [0]* len(arr)
    #traverse from back.
    for i in range(len(arr)-1,-1,-1):
        output_array[count_array[arr[i]]-1] = arr[i]
        count_array[arr[i]] -= 1
    return output_array
if __name__ == "__main__":
    arr = [4, 3, 12, 1, 5, 5, 3, 9]
    print(counting_sort(arr))
#TC : O(N+M).SC : O(N+M).   



