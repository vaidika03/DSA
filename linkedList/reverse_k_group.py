#12. Reverse a LinkedList in groups of size k.
def findSize(head):
    tmp = head
    check = 0
    while tmp:
            tmp = tmp.next
            check += 1
    return check

def reverse_k_group(head, k):
    if head is None or k ==1:
            return head
    curr = head
    newHead = None
    tail = None
    size = findSize(head)
    reverseCount = (size // k)
    while curr:
        groupHead = curr
        count = 0
        prev = None       
        if reverseCount > 0:
            while curr and count<k:
                #print(curr.val)
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1
            if reverseCount >0:
                if newHead is None:
                    newHead = prev
                if tail is not None:
                    tail.next = prev
                tail = groupHead
            reverseCount -= 1
        else:
            if tail:
                tail.next = groupHead
            break
    return newHead

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head = reverse_k_group(head, 4)
    print("12. reverse_k_group:",end ="")
    print_list(head)
