#18. Flattening of a LinkedList
class Node:
    def __init__(self, new_val):
        self.val = new_val
        self.next = None
        self.bottom = None
def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

def flatten(head):
    curr = head
    values = []
    while curr is not None:
        values.append(curr.val)
        bottom_curr = curr.bottom
        while bottom_curr is not None:
            values.append(bottom_curr.val)
            bottom_curr = bottom_curr.bottom
        curr = curr.next
    #sort values
    values.sort()
    tail = None
    newHead = None
    for value in values:
        newNode = Node(value)
        if newHead is None:
            newHead = newNode
        else:
            tail.next = newNode
        tail = newNode
    return newHead

head = Node(5)
head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)

head.next = Node(10)
head.next.bottom = Node(20)

head.next.next = Node(19)
head.next.next.bottom = Node(22)
head.next.next.bottom.bottom = Node(50)

head.next.next.next = Node(28)
print("18. Flatten List:",end = " ")
print_list(flatten(head))

