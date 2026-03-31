from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = defaultdict(int)

        for st in s:
            if st in hash_map:
                hash_map[st] += 1
            else:
                hash_map[st] = 1

        for i, ch in enumerate(s):
            if hash_map[ch] == 1:
                return i

        return -1