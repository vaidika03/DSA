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
