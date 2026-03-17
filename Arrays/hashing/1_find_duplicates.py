class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}

        # Build frequency map
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Collect duplicates
        duplicates = []
        for key in freq:
            if freq[key] > 1:
                duplicates.append(key)

        return duplicates