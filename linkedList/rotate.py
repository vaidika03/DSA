#13. Rotate a LinkedList

def rotate(head, degree): 
    if not head or not head.next:
        return head
    cur = head
    length = 1
    while cur and cur.next:
        cur = cur.next
        length +=1

    degree = length - degree % length - 1
    tail = cur
    tail.next = head
    cur = head
    while degree:
        cur = cur.next
        degree-=1
    new_head = cur.next
    cur.next = None
    return new_head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = rotate(head, 2)
    print("13. right rotate a linkedList:",end = "")
    print_list(head)
