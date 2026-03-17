#Time Complexity: O(n) for add, remove, contains operations.
#Space Complexity: O(n) for the hash list.
class MyHashSet:

    def __init__(self):
        self.hash = []
        
    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hash
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
#-----------------------------------

class MyHashSet:

    def __init__(self):
        self.hash = [[] for _ in range(10)]
        

    def add(self, key: int) -> None:
        bucket_index = key % 10
        if key not in  self.hash[bucket_index]:
            self.hash[bucket_index].append(key)
        

    def remove(self, key: int) -> None:
        bucket_index = key % 10
        if key in  self.hash[bucket_index]:
            self.hash[bucket_index].remove(key)

        

    def contains(self, key: int) -> bool:
        bucket_index = key % 10
        return key  in  self.hash[bucket_index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)