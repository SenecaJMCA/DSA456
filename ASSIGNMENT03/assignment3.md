ASSIGNMENT 3 - PART A

Part A: Analyze the following functions concerning the number of Records stored in the SortedTable

    Before analyzing each function lets assume that n is the number of records of the table and C is total capacity of the table.

    def __len__(self): this function will use a constant to loop over the entire table, therefore it time complexity is O(C)

    def search(self, key): this is a linear search because uses a while loop to scan the table, therefore the constant used in the fucntion has a O(C) and since has to run it n times the process is O(n). SO it has a time complexity of O(n)

    def insert(self, key, value): the first thing this fx does is to call the search fx, so we can attribute an order O(n), then the capacity is checked wiht a cost of constant => O(C), if it's full it will resize the table then will have to run it for n times O(n), then it wiould insert the new key-value with a performance of O(n), and lastly do a buble sort and sawpping key-values  with cost of O(n2). That whole math leave us with a function with time complexity of O(n2) (quadractic fucntion)

    def modify(self, key, value): it first checks the length so it cost O(C) and then it loops through the table to find a possible matching value so it cost O(n). Therefore making the cost of O(n)

    def remove(self, key): this fucntion will fist need to search for the given key, for that it performs a len() with cost of O(n) and then loops throught the table, another O(n). Once that's completed it comes the shifting task with also a time complexity of O(n). At the end we have O(n)+O(n)+O(n), which simplifing we get a total time complexity of O(n), sicne the constants won't affect the magnitude of it.

    def capacity(self): this functions performs basically the len() function to get the table capacity, in other words is only has a time complexity of (1).


    Summary:
    def __len__(self): O(C)

    def search(self, key): O(n)

    def insert(self, key, value): O(n2) (quadractic fucntion)

    def modify(self, key, value): O(n)

    def remove(self, key): O(n)

    def capacity(self): O(1)

IMPROVEMENTS FOR PART A

- In term of the search function instead of using a bubble search we could use a binary search to improve the time complexity, this way the time complexity would go from O(n) to O(log n)
- Having the the function _len_() being called several times inside the fucntions made the process cost O(n), instead we could set the self.size and this way the time complexity would drop from to a constant cost O(1). Ths would avoid us to repeat over and over again, one of the principles of coding.
- The insertion fucntion does a unecessary buble sort before inserting a new key, for that we could just look for the right index using a binary search and shift elements to create room for the new element, that would make the insert function jump from O(n2) to a O(n) time complexity.
