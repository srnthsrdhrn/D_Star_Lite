class Heap():
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0
        
    def heapify(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                temp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2] 
                self.heaplist[i // 2] = temp
            i=i // 2
    
    
    def insert(self, key):
        self.heaplist.append(key)
        self.currentSize += 1
        self.heapify(self.currentSize)