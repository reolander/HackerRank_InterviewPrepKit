def sortedInsert(head, data):
    new_element = DoublyLinkedListNode(data)
    if head:
        current = head 
        if current.data > new_element.data:
            new_element.prev = None
            new_element.next = current
            current.prev = new_element
            return new_element
        else:
            while current and current.data <= new_element.data:
                previous = current
                current = current.next
            new_element.next = previous.next
            new_element.prev = previous
            previous.next = new_element
            return head 
    else:
        head = new_element
        return head