#Time Complexity: O(n log n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        d = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
        
        result = ''
        for char, freq in d:
            result += char * freq
        return(result)



'''
What d.items() gives you
If d = {'a': 3, 'b': 1, 'c': 2}, then d.items() returns pairs:


[('a', 3), ('b', 1), ('c', 2)]
Each pair is (key, value) → (character, frequency).

What lambda kv: kv[1] means
Think of lambda as a mini throwaway function. It takes one input and returns one output:


lambda kv: kv[1]
       ↑      ↑
    input    output
kv = one pair, e.g. ('a', 3)
kv[0] = 'a' (the character)
kv[1] = 3 (the frequency)
So key=lambda kv: kv[1] tells sorted(): "sort by the second element (the frequency)".

How to remember it
Think of it as answering one question:

"Sort BY what?"


sorted(stuff, key=lambda item: item[____], reverse=True)
                                      ↑
                              0 = sort by key
                              1 = sort by value
reverse=True → biggest first (descending)
reverse=False (default) → smallest first (ascending)
A handy way to remember

sorted(d.items(), key=lambda kv: kv[1], reverse=True)
       ↑                           ↑          ↑
  "give me pairs"        "sort by value"   "biggest first"
That's it — pairs in, sort by position, pick direction.'''