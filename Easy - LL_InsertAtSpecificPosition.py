# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data); current = head; pos = 0
    if head:
        if position > 1:
            while current.next and pos < position - 1:
                current = current.next
                pos += 1
            node.next = current.next
            current.next = node
            return head            
        elif position == 1:
            node.next = head.next
            head = node
            return head
    else:
        head = data
        return head
