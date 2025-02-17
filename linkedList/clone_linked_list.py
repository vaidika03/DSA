#19. Clone a Linked List with random and next pointer
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
    
def clone_linked_list(head):
    if head is None:
        return None
    #add duplicate node nd insert them next to original
    curr = head
    while curr:
        newNode = Node(curr.val)
        newNode.next = curr.next
        curr.next = newNode
        curr = newNode.next
    #clone random pointer in newNode
    curr = head
    while curr:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next

    #seperate list
    curr = head
    cloned_head = head.next
    cloned = cloned_head
    while cloned.next is not None:
        curr.next = curr.next.next
        cloned.next = cloned.next.next 
        curr = curr.next
        cloned = cloned.next
    curr.next = None
    cloned.next = None

    return cloned_head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next
print("19. clone_linked_list:",end = " ")
print_list(clone_linked_list(head))
