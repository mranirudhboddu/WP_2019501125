class LRU:
    
    def __init__(self,capacity):
        super().__init__()
        self.capacity=capacity
        self.cache={};
        self.caches={};

    def put(self, key, value):
        if key not in self.cache and len(self.cache)==self.capacity:
            old=min(self.caches.keys(),key=lambda k:self.caches[k])
            self.cache.pop(old)
            self.caches.pop(old)
        self.cache[key] = value
        self.caches[key]=1
        return "Data entered"

    def get(self, key):
        if key in self.cache:
            self.caches[key]=self.caches[key]+1
            return self .cache[key]
        else:
            print("not found in cache")    

    def  get_cache(self):
        return self.cache

    # if __name__ == "_main_":
    #     dict=LRU(3)
    #     dict.put(1,"anirudh")
    #     dict.put(2,"boddu")
    #     dict.put(3,"sanjana")
    #     print(dict.get(1))
    #     print(dict.get(2))
    #     print(dict.get(3))

    #     dict.put(4,"rao")
    #     dict.put(5,"madhavi")    
    #     print(dict.get_cache())