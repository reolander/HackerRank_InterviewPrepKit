"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    current, fast = head, head
    if head:
        while fast and fast.next:
            current = current.next
            fast = fast.next.next
            
            if fast == current:
                return True
        else:
            return False
    else:
        return False