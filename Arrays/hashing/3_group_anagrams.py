#Approach 1: The Counting Approach (HashMap)
#Time complexity: O(n)
#Space complexity: O(1)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            #making it tuple because list cannot be used as a dict key
            key = tuple(sorted(word))
            groups[key].append(word)
        return list(groups.values())
        
#---------------------------    
#Time complexity:  O(n · k)
#Space complexity: O(n · k)
#Approach 2: Counting Key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            #making key as a number counting list (converting it to tuple)
            count = [0] * 26

            for char in word:
                #updating count as list format
                count[ord(char) - ord('a')] += 1
            #converting list to tuple because list cannot be used as a dict key
            key = tuple(count)
            groups[key].append(word)
        return list(groups.values())

        