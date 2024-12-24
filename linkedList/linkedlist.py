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
#delete Middle Node
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
#Find the middle of LinkedList   
def findMiddle(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next        
    return slow.val

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
    print("2. middle of Linked list:", end="")
    print(findMiddle(head))
    print("3. delete middle node:",end = "")
    print_list(deleteMiddleNode(head))
    
#-------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
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
#-------------------------------------------------------------------
#6. Delete a given Node when a node is given.(0(1) solution)
def deleteNode(delNode):
    if delNode is None or delNode.next is None:
        return     
    nextNode = delNode.next
    delNode.val = nextNode.val
    delNode.next = nextNode.next
    
if __name__ == "__main__":    
    # Creating a linked list: 4 -> 5 -> 6 -> 7 -> 8
    head = Node(4)
    head.next = Node(5)
    head.next.next = Node(6)
    head.next.next.next = Node(7)
    head.next.next.next.next = Node(8)
    deleteNode(head)
    print("6. deleteNode:",end=" ")
    print_list(head)
#-------------------------------------------------------------------------    
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
#---------------------------------------------------------------
#8 Detect a cycle in Linked List
def detect_loop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ =="__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    head.next.next.next.next = head
    print("8. detect_loop:",detect_loop(head))
#-------------------------------------------------------------
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
#-------------------------------------------------------------------
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
#-------------------------------------------------------------
#11.Add two numbers as LinkedList
def countNodes(head):
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next
    return length

def addTwoLists(num1, num2):
    n1 = countNodes(num1)
    n2 = countNodes(num2)
    
    carry = 0
    if n1<n2:
        num1,num2 = num2,num1
    res = num1
    
    while num1 or carry!=0:
        num1.val += carry
        if num2:
            num1.val+=num2.val
            num2 = num2.next
        carry = num1.val // 10
        num1.val = num1.val % 10
        if num1.next is None and carry!=0:
            num1.next = Node(0)
        num1 = num1.next
    return res
            
#list is already reversed.so no need to reverse list
if __name__ == "__main__":
    num1 = Node(9)
    num1.next = Node(9)
    num1.next.next = Node(9)
    num1.next.next.next = Node(9)
    num1.next.next.next.next = Node(9)
    num1.next.next.next.next.next = Node(9)
    num1.next.next.next.next.next.next = Node(9)

    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)
    num2.next.next.next = Node(9)
    sum_list = addTwoLists(num1, num2)
    print("11. Add two Numnbers",end = " ")
    print_list(sum_list)
#----------------------------------------------------------------    
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
    
#-----------------------------------------------------
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
#-----------------------------------------------------
#14. Remove Duplicate from Sorted array
def removeDuplicates(nums):
    k = 1
    res = []
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return nums[:k]

nums = [1,1,2]
print("14. Remove duplicates inplace:",removeDuplicates(nums))
#-------------------------------------------------------------------------
#15. Max consecutive ones
def findMaxConsecutiveOnes(nums):
    maxi = count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > maxi:
                maxi = count
            count = 0
    return max(maxi, count)

nums = [1,1,0,1,1,1]
print("15. findMaxConsecutiveOnes:",findMaxConsecutiveOnes(nums))
#---------------------------------------------------------------------------
#16. 3 sum
def threeSum(arr) :
        arr.sort()
        triplets = []
        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate elements
                continue
            l, r = i + 1, len(arr) - 1
            while l < r:
                curr_sum = arr[i] + arr[l] + arr[r]
                if curr_sum == 0:
                    triplets.append([arr[i], arr[l], arr[r]])
                    while l < r and arr[l] == arr[l + 1]:  # Skip duplicate elements for 'l'
                        l += 1
                    while l < r and arr[r] == arr[r - 1]:  # Skip duplicate elements for 'r'
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return triplets
nums = [-1,0,1,2,-1,-4]
print("16. 3 sum:",threeSum(nums))
#----------------------------------------------------------
#17. Trapping Rainwater
def trap(arr):
        n = len(arr)
        left_max = 0
        right_max = 0
        left, right = 0, n - 1
        res = 0
        idx = 0
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    res += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    res += right_max - arr[right]
                right -= 1     
        return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("17. Trapping Rainwater:",trap(height))
