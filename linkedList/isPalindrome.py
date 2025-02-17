#9. Check if a LinkedList is palindrome or not.
"""
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def isIdentical(n1, n2):
    while n1 and n2:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next
    return True

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    head2 = reverse(slow.next)
    ret = isIdentical(head, head2)
    head2 = reverse(head2)
    slow.next = head2
    return ret
"""
def isPalindrome(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next

    return l == l[::-1]
if __name__ == "__main__": 
    # Linked list : 1->2->3->2->1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    print("9.isPalindrome:",isPalindrome(head))
