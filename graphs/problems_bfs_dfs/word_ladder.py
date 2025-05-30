from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #base condition
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        wordSet = set(wordList)
        pattern_map = defaultdict(list)

        #make pattern dictionary
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        #fill queue
        queue = deque([(beginWord,1)])
        visited = set([beginWord])


        #Run BFS
        while queue:
            word, level = queue.popleft()
            for i in range(L):
                #create a pattern with the current word present in the queue
                pattern = word[:i] + '*' + word[i+1:]
                #check for the pattern created and words associated with it and if the word matches with the endWord
                for neighbour in pattern_map[pattern]:
                    if neighbour == endWord:
                        return level + 1
                    #if the word associated with the pattern is not visited, add it to the queue and mark it as visited
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, level + 1))
                #after checking all the words associated with the pattern, clear the pattern map to avoid reprocessing
                pattern_map[pattern] = []
        return 0



        