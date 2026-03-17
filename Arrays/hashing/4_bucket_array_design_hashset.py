#Time Complexity: O(1) for add, remove, contains operations.
#Space Complexity: O(n) for the hash list.


class MyHashSet:
    def __init__(self):
        #Make Bucket Array of size 10
        self.hash = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        #Get the bucket index
        bucket_index = key % 10
        #If the key is not at the index of the bucket (list of the bucket), add it
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