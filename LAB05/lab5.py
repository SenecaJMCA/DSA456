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
        


# PART B
# Analysing the above functions where T(n) and O (n) is the size of the linked list, where n is the size of the array
    
# 1.__init__:
#     Constant operation, assigning self.head to None
#     T(n) = c
#     O(n) = O(1)

# 2. is_empty 
#     Constant operation, checking if self.head is None
#     T(n) = c
#     O(n) = O(1)

# 3. prepend:
#     Constant operation, creates a node and update couple of reference
#     T(n) = c
#     O(n) = O(1)

# 4. append:
#     Considering the worse case, it would iterate the entire list to find the las node
#     T(n) = an + b
#     O(n) = O(n)

# 5. insert_after:
#     Assuming we already know the target node the insertion time is a constant operation
#     T(n) = c
#     O(n) = O(1)

# 6. delete:
#     The worse case scenaruio would it be to have to delete the last node of the ranked list, therefore to iterate the entire list
#     T(n) = an + b
#     O(n) = O(n)


# 7. search:
#     The worse case scenario would be to either not found the target node or item is not in the list(not found). Again another iteration throught the entire list
#     T(n) = an + b
#     O(n) = O(n)

# 8. size:
#     Another interation of the entire list to count the number of nodes
#     T(n) = an + b
#     O(n) = O(n)

# 9. to_list:
#     Another entire interation to append items to a list
#     T(n) = an + b
#     O(n) = O(n)

# 10. print:
#     Another interation of the entire list to print all items
#     T(n) = an + b
#     O(n) = O(n)


