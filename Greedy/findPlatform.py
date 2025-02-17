#2. Program to find minimum number of platforms required on a railway station
def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1
        elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1
        if (plat_needed > result):
            result = plat_needed
    return result
arr = [100, 300, 500]
dep = [900, 400, 600]
n = len(arr)
print("2. platform needed:",findPlatform(arr, dep, n))
