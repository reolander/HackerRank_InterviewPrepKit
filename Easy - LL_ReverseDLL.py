# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    current = head;
    while current.next:
        temp = current.next
        current.next = current.prev
        current.prev = temp
        current = current.prev
    current.next = current.prev
    current.prev = None
    return current
    