'''
Time Complexity: O(n) where n = len(nums). The loop runs 2n iterations, and each index is pushed/popped from the stack at most twice, so the stack operations are O(n) overall. The result construction is also O(n).
Space Complexity: O(n) for the stack (up to 2n elements in the worst case, but still O(n)), the next_greater_elm_idx dictionary (up to n entries), and the result list.
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater_elm_idx = {}
        for i in range(2* len(nums)):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                waiting_elem_idx = stack.pop()
                next_greater_elm_idx[waiting_elem_idx] = i % len(nums)
            stack.append(i % len(nums))

        result = []
        for n in range(len(nums)):
            if n in next_greater_elm_idx:
                result.append(nums[next_greater_elm_idx[n]])
            else:
                result.append(-1)
        return result


                
        