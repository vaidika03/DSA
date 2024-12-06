#2.Find Whether an Array is a Subset of Another Array
# TC: O(N) , SC: O(N)
def check_subset(arr1, arr2):
    arr1 = set(arr1)
    for num in arr2:
        if not num in arr1:
            return False
    return True

if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 8, 1]
    print(check_subset(arr1, arr2))
