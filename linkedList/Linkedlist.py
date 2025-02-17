class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None
        
# Function to print the linked list
def print_list(head):
    while head is not None:
        print(f"{head.val}(", end="")
        if head.random:
            print(f"{head.random.val})", end="")
        else:
            print("null)", end="")
        
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()
