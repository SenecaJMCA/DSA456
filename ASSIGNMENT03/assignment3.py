class ChTable:
    class Record:
        def __init__(self,key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
            self.table = [[] for _ in range (capacity)]
            self.cap = capacity
            self.size = 0

    def insert(self, key, value):
        if self.search(key) is not None:
                return False
            
        if (self.size + 1) / self.cap > 1.0 :
                self._grow_table()

        idx = hash(key) % self.cap
        new_record = self.Record(key, value)
        self.table[idx].append(new_record)
        self.size = self.size + 1
        return True
        
    def _grow_table(self):
        old_table = self.table
        self.cap = self.cap * 2
        self.table = [[] for _ in range(self.cap)]
        self.size = 0

        for bucket in old_table:
            for record in bucket:
                self.insert(record.key, record.value)

    def modify(self, key, value):
        idx = hash(key) % self.cap
        chain = self.table[idx]
        for record in chain:
            if record.key == key:
                record.value = value
                return True
        return False
        
    def remove(self, key):
        idx = hash(key) % self.cap
        chain = self.table[idx]
        for i in range(len(chain)):
            if chain[i].key == key:
                chain.pop(i)
                self.size = self.size - 1
                return True
        return False
        
    def search(self, key):
        idx = hash(key) % self.cap
        chain = self.table[idx]
        for record in chain:
            if record.key == key:
                return record.value
        return None
        
    def capacity(self):
        return self.cap
        
    def __len__(self):
        return self.size
        


# -----------------   TESTING THE CODE ----------------

t = ChTable()

print(t.insert("a", 14))   
print(t.insert("b", 25))   
print(t.insert("a", 39))   
print(t.search("a"))      
print(t.modify("a", 140))  
print(t.search("a"))      
print(t.remove("a"))      
print(t.search("a"))      
print(len(t))             
print(t.capacity())       