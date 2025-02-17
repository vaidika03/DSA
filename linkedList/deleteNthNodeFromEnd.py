#5. remove N-th node from back of LinkedList
def deleteNthNodeFromEnd(head, n):
    curr = head
    prev = head
    size = 0
    while curr:
        size+=1
        curr = curr.next
    idx = size-n
    if idx == 0:
        return head.next
    curr = head
    for i in range(idx):
        prev = curr
        curr = curr.next

    prev.next = curr.next
    return head

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("5. delete Nth Node From End:")
    # print("Linked List before Deletion:")
    # print_list(head)
    head = deleteNthNodeFromEnd(head, 4)
    print("Linked List after Deletion:")
    print_list(head)
