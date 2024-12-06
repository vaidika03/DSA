#3. Find the Missing And Repeating Element
def print_two_elements(arr,n):
    n = len(arr)
    missing = (n * (n + 1)) // 2 
    print("Repeating", end=" ")

    for i in range(n):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            missing -= abs(arr[i])  # subtract unique elements
        else:
            print(abs(arr[i]))

    print("Missing", missing)
if __name__ == "__main__":
    arr = [7, 3, 4, 5, 5, 6, 2]
    n = len(arr)
    print_two_elements(arr,n) 
