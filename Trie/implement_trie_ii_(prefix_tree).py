#Time Complexity: O(m) for insert, countWordsEqualTo, 
# countWordsStartingWith, and erase where m is the length of the word or prefix.
#Space Complexity: O(m) for the Trie structure where m is the total number of characters``
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.prefix_count = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count
        

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) == 0:
            return
        node = self.root
        for char in word:
            next_node = node.children[char]
            next_node.prefix_count -= 1     # decrement prefix count
            # Optional: cleanup nodes with prefix_count == 0 to save space
            node = next_node
        node.word_count -= 1                # decrement exact word count
 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)