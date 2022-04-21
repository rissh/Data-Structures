
class MyHashSet:

    def __init__(self):
        self.hs = 0
    
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hs += 1<<key
    
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hs -= 1<<key
    
    def contains(self, key: int) -> bool:
        return (self.hs>>key)&1
      