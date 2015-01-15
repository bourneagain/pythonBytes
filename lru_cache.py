REMOVED = '<removed-key>'
# @param capacity, an integer
def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    self.pq = []
    self.size = 0
    self.counter = 0

# @return an integer
def get(self, key):
    if key not in self.cache:
        return -1
    priority, key, value = self.cache[key]
    if priority != self.counter:
        self.remove(key)
        self.add(key, value)
    return value

def remove(self, key):
    entry = self.cache.pop(key)
    entry[1] = self.REMOVED

def add(self, key, value):
    self.counter += 1
    entry = [self.counter, key, value]
    self.cache[key] = entry
    heapq.heappush(self.pq, entry)

# @param key, an integer
# @param value, an integer
# @return nothing
def set(self, key, value):
    if key in self.cache:
        self.remove(key)
    else:
        if self.size < self.capacity:
            self.size += 1
        else:
            while self.pq:
                _, k, _ = heapq.heappop(self.pq)
                if k is not self.REMOVED:
                    del self.cache[k]
                    break
    self.add(key, value)