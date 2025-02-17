#10. Find the starting point of the Loop of LinkedList
def detectLoop(head) :
    slow, fast = head, head
    
    # Step 1: Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Cycle detected, now find the start of the cycle
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # The start of the cycle
    
    return None 

head = Node(10)
head.next = Node(15)
head.next.next = Node(4)
head.next.next.next = Node(20)

head.next.next.next.next = head

loopNode = detectLoop(head)
print("10. detectLoop:",loopNode.val)
