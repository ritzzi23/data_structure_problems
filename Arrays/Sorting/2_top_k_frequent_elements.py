"""
Sorting -- O(n log n) time, O(n) space
Count frequencies, sort by frequency, take top k. Simplest but slowest.

Heap -- O(n log k) time, O(n) space
Count frequencies, maintain a min-heap of size k. Better than sorting when k is small relative to n.

Quickselect -- O(n) average time, O(n) space
Partition-based selection on frequency. Average O(n) but worst case O(n^2).

Bucket Sort -- O(n) time, O(n) space
Use frequency as bucket index, walk buckets from right to left. Guaranteed O(n), no worst case pitfall. Best approach for interviews.
"""


from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        