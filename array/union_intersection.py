#3. Find the Union and Intersection of Two Sorted Arrays
# TC : O(N) , SC : O(n+m) 
"""
def union_array(a,b):
    a,b = set(a),set(b)
    return list(a | b)

def intersection_array(a,b):
    a,b = set(a),set(b)
    return list(a & b)
"""
def union_array(a,b):
    union = []
    for item in a+b:
        if item not in union:
            union.append(item)
    return union

def intersection_array(a,b):
    intersection = []
    for item in a:
        if item in b and item not in intersection:
            intersection.append(item)
    return intersection       

if __name__ == "__main__":
    a,b = [1, 1, 2, 2, 2, 4],[2, 2, 4, 4]
    print("union_array:",union_array(a,b)) 
    print("intersection_array:",intersection_array(a,b)) 
