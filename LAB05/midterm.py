# 1 Median list
# def find_median(lst):
#     sorted_lista = sorted(lst)
#     n=len(sorted_lista)
#     mid = n//2

#     if n % 2 == 1:
#         return sorted_lista[mid]
#     else:
#         return (sorted_lista[mid-1] + sorted_lista[mid]) / 2
    

# list1 = [5,4,8,2,9,1,3]
# list2 = [4,5,2,1,8,9]

# print(find_median(list1))
# print(find_median(list2))
    
# 2 Pell function
# def pell(n):
#     # P(n) = 2*P(n-1) + P(n-2)
#     # Defining the bases cases
#     if n<0:
#         return print("Invalid number")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     p0 = 0
#     p1 = 1
#     for _ in range(2, n+1):
#         pn = 2*p1 + p0
#         p0 = p1
#         p1 = pn

#     return p1

# for i in range(10):
#     print(pell(i))


# 3 Fibonacci function
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for i in range(10):
#     print(fibonacci(i))


# 7 Clone functions
class LList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.front = None
        self.back = None

    def insert_back(self, data):
        new_node = self.Node(data)
        if self.front is None:
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def __str__(self):
        vals = []
        cur = self.front
        while cur:
            vals.append(str(cur.data))
            cur = cur.next
        return " -> ".join(vals)

    @staticmethod
    def clone_range_index(myLList, i, j):
        new_list = LList()
        if i < 1 or j < i:
            return new_list

        current = myLList.front
        pos = 1

        while current is not None and pos <= j:
            if pos >= i:
                new_list.insert_back(current.data)
            current = current.next
            pos += 1

        return new_list

    @staticmethod
    def clone_range(myLList, min_value, max_value):
        new_list = LList()
        current = myLList.front
        while current is not None:
            if min_value <= current.data <= max_value:
                new_list.insert_back(current.data)
            current = current.next
        return new_list


myLList = LList()
for value in [10, 25, 5, 40, 15, 30]:
    myLList.insert_back(value)

clone1 = LList.clone_range_index(myLList, 2, 4)
print(clone1)  

clone2 = LList.clone_range(myLList, 10, 25)
print(clone2)  