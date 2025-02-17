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
