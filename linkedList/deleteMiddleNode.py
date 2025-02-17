def deleteMiddleNode(head):
    if head is None or head.next is None:
            return None
    fast = head
    slow = head
    prev = None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next   
    prev.next = slow.next     
    return head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    print_list(head)
    print("3. delete middle node:",end = "")
    print_list(deleteMiddleNode(head))
