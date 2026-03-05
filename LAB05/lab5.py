from typing import Any, Optional, List

class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head= None

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data: Any):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, target: Node, data: Any):
        if target is None:
            return
        
        new_node = Node(data)
        new_node.next = target.next
        target.next = new_node

    def delete(self, target: Node) -> bool:
        if self.head is None or target is None:
            return False
        
        if self.head == target:
            self.head = self.head.next
            return True
        
        prev = self.head
        current = self.head.next

        while current is not None and current != target:
            prev = current
            current = current.next

        if current is None:
            return False
            
        prev.next = current.next
        return True

    def search(self, data: Any) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def to_list(self) -> List[Any]:
        result = List[Any] = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def print(self) :
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
        