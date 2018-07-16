class Node:
    __refs__ = defaultdict(list)
    __start__ = None
    __goal__ = None
    __queue__ = []
    def __init__(self, x, y,is_start = False,is_goal = False):
        self.__refs__[self.__class__].append(weakref.ref(self))
        self.x = x
        self.y = y
        self.k = 0
        self.h = 0
        self.g = 0
        self.rhs = 0
        self.neighbours = []
        self.calculate_neighbours()
        self.g_count = 0
        self.h_count = 0
        if is_start:
            self.__start__ = self
        if is_goal:
            self.__goal__ = self
        
    def computeKey(self):
        self.k = [min(self.g,self.rhs)+self.h,min(self.g,self.rhs)]
        

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst
    
    def calculate_neighbours(self):
        for node in Node.get_instances():
            for i in range(self.x-1,self.x+1):
                for j in range(self.y-1,self.j+1):
                    if i == self.x and j == self.y:
                        continue
                    if i == node.x and j == node.y:
                        self.neighbours.append(node)
    @classmethod
    def enqueue(cls,a):        
        cls.__queue__.insert(0,a)
    
    @classmethod
    def dequeue(cls)
        return cls.__queue__.pop()
    
    @classmethod
    def calculate_g(cls):
        cls.__start__.g_count+=1
        cls.enqueue(cls.__start__)
        while cls.__queue__.__len__()>0:
            current_node = cls.dequeue()
            for node in current_node.neighbours:
                
        