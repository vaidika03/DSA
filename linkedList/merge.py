#4.Merge two sorted Linked List (use method used in mergeSort)
def merge_util(list1,list2):
    if not list1.next:
        list1.next = list2
        return list1

    curr1, next1 = list1, list1.next
    curr2, next2 = list2, list2.next

    while curr2 and next1:
        if curr2.val>=curr1.val and curr2.val<=next1.val:
            next2 = curr2.next
            curr1.next = curr2 
            curr2.next = next1     
            curr1 = curr2
            curr2 = next2
        else:
            if next1.next:
                next1 = next1.next
                curr1 = curr1.next
            else:
                next1.next = curr2
                return list1
    return list1

def merge(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        return merge_util(list1,list2)
    else:
        return merge_util(list2,list1)
    
if __name__ == "__main__": 
    # 1->3->5 LinkedList created
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)
    # 0->2->4 LinkedList created
    list2 = Node(0)
    list2.next = Node(2)
    list2.next.next = Node(4)
    res = merge(list1, list2)
    print("4. Merge two sorted Linked List:",end=" ")
    print_list(res)
