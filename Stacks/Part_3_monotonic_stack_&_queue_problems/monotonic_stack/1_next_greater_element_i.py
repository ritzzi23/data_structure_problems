'''
Time Complexity: O(n + m) where n = len(nums2) and m = len(nums1). Each element in nums2 is pushed and popped from the stack at most once, so the stack processing is O(n). The lookup loop for nums1 is O(m) with O(1) dict lookups.
Space Complexity: O(n) for the stack and the next_greater dictionary, both of which can hold up to n elements. The result list is O(m), so overall O(n + m).
'''
#All integers in nums1 and nums2 are unique.

# Monotonic Stack (Decreasing) Solution for Next Greater Element I
# LeetCode 496
#
# Problem: For each element in nums1, find the next greater element in nums2.
#          nums1 is a subset of nums2.
#
# Example:
#   nums1 = [1, 2],  nums2 = [4, 1, 2, 3]
#   Output: [2, 3]
#   Explanation:
#     1 -> next greater in nums2 after 1 is 2 -> 2
#     2 -> next greater in nums2 after 2 is 3 -> 3

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack: list[int] = []  # Waiting room: numbers waiting to find their boss
        next_greater = {}   # Maps each number -> its next greater element (boss)

        # Walk through every number in nums2, left to right
        for num in nums2:

            # The new arrival (num) checks with people at the BACK of the waiting room.
            # If the new arrival is BIGGER, it becomes their boss -> evict them.
            # Keep evicting until we hit someone bigger than us, or the room is empty.
            while stack and stack[-1] < num:
                waiting_elem = stack.pop()          # This person found their boss!
                next_greater[waiting_elem] = num    # Record: waiting_elem's boss is num

            # New arrival sits at the back, waiting for their own boss
            stack.append(num)

        # Anyone still in the waiting room never found a boss -> their answer is -1
        # (no need to explicitly handle this; dict.get() returns -1 as default below)

        # For every number in nums1, look up its boss in our dictionary
        # If not found (still in waiting room), return -1
        # Same thing, written out plainly
        result = []
        for n in nums1:
            if n in next_greater:
                result.append(next_greater[n])   # found a boss → add it
            else:
                result.append(-1)                # no boss found → add -1
        return result



# ─── Dry Run ────────────────────────────────────────────────────────────────
# nums2 = [4, 1, 2, 3]
#
# num=4  | stack=[]        -> nobody to evict | stack=[4]     | next_greater={}
# num=1  | stack=[4]       -> 1 < 4, stop     | stack=[4,1]   | next_greater={}
# num=2  | stack=[4,1]     -> 2 > 1, evict 1  | stack=[4,2]   | next_greater={1:2}
# num=3  | stack=[4,2]     -> 3 > 2, evict 2  | stack=[4,3]   | next_greater={1:2, 2:3}
#                          -> 3 < 4, stop
#
# Leftover in stack: [4, 3] -> they never found a boss -> return -1 for them
#
# nums1 = [1, 2]
# Result: [next_greater[1], next_greater[2]] = [2, 3]  ✅