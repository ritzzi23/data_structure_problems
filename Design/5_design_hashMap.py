#Time Complexity: O(1) for put, get, remove operations.
#Space Complexity: O(n) for the hash list.

class MyHashMap:

    def __init__(self):
        #Make Bucket Array of size 10
        self.hashMap = [[] for _ in range(10)]
        
    def put(self, key: int, value: int) -> None:
        bucket_index = key % 10
        #using enumerate to get the index of the key in the bucket (specifically a particular place in the list)
        for i, (k,v) in enumerate(self.hashMap[bucket_index]):
            #If the key is already in the bucket, update the value
            if k == key: 
                self.hashMap[bucket_index][i] = (key,value)
                #return once the key is found and updated
                return
        #If the key is not in the bucket, add it to the bucket at the end
        self.hashMap[bucket_index].append((key,value))
        

    def get(self, key: int) -> int:
        bucket_index = key % 10
        for (k,v) in self.hashMap[bucket_index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % 10
        for (k,v) in self.hashMap[bucket_index]:
            if k == key:
                #remove function is used to remove the key-value pair from the bucket
                self.hashMap[bucket_index].remove((k,v))
        return -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)