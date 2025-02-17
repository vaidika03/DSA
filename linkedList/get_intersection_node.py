#7. Find intersection point of Y LinkedList
"""
def get_intersection_node(head1, head2):
    ptr1 = head1
    ptr2 = head2

    if not ptr1 or not ptr2:
        return None

    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

    return ptr1
"""
def get_intersection_node(head1, head2):
    def get_count(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    l1,l2 = get_count(head1),get_count(head2)
    if l1>l2:
        for _ in range(l1-l2):
            head1 = head1.next
    else:
        for _ in range(l2-l1):
            head2 = head2.next
    while head1 and head2:
        if head1 == head2:
            return head1
        head1, head2 = head1.next, head2.next
    return None
    
    
if __name__ == "__main__":
    # Creation of the first list
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)
    # Creation of the second list
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)
    head2.next.next.next = head1.next 
    res = get_intersection_node(head1, head2)
    print("7. get_intersection_node:",res.val)
