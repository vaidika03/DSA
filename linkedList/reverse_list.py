#Reverse a LinkedList
def reverse_list(head):
    curr = head
    prev = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode   
    return prev  


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    print_list(head)
    head = reverse_list(head)
    print("1. reversed Linked list:", end="")
    print_list(head)
