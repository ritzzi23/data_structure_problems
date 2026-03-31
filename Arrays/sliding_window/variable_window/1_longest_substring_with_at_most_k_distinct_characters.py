'''
Approach 1: Brute Force
Generate all possible substrings.
For every substring, count how many distinct characters it has.
If distinct characters are <= k, update the maximum length.
This works because we check every possible substring.
It is slow because there are many substrings, and for each one we may scan again to count distinct characters.
Time Complexity: O(n^3)
Space Complexity: O(n) in worst case for storing substring/set

Approach 2: Better Brute Force
Fix a starting index i.
Extend the substring one character at a time using index j.
Maintain a frequency map or set while expanding, instead of recomputing from scratch.
For each start index, we keep growing and checking distinct characters.
This is better because we reuse previous work for the same starting point.
Still slow, because for every i we may scan far to the right.
Time Complexity: O(n^2)
Space Complexity: O(k) or O(min(n, charset))

Approach 3: Sliding Window
Use two pointers: left and right.
Expand the window by moving right.
Keep a frequency map of characters inside the current window.
If distinct characters become more than k, shrink the window from the left until it becomes valid again.
At every valid window, update the maximum length.
This is best because each character is added once and removed at most once.
Very natural for longest substring with a condition.
Time Complexity: O(n)
Space Complexity: O(k) or O(min(n, charset))

Best approach
Sliding window is the optimal approach.
Reason:
substring is contiguous
we need longest length
condition depends on current window's distinct character count
'''


#Optimal Solution
#Time Complexity: O(n)
#Space Complexity: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0
        j = 0
        longest_substring = {} #Space Complexity: O(k)
        max_count = 0
        while (j < len(s)): #Time Complexity: O(n)
            #calculations to make our statement 
            if s[j] not in longest_substring:
                longest_substring[s[j]] = 0
            longest_substring[s[j]] += 1
            #condition
            #we try to firstly make a valid window
            if (len(longest_substring) < k):
                max_count = max(max_count,(j-i+1)) #Time Complexity: O(1)
                j += 1
            #condition
            #when our condition is reached
            elif (len(longest_substring) == k):
                max_count = max(max_count,(j-i+1))
                j += 1
            #When window seize to remain valid
            elif (len(longest_substring) > k):
                #we make operations till the window again becomes valid
                while ( len(longest_substring) > k):
                    #remove calculations for i to make the contion correct again 
                    longest_substring[s[i]] -= 1
                    if longest_substring[s[i]] == 0:
                        del longest_substring[s[i]]
                    #meanwhile we shrink the window from left side to make the window valid 
                    i += 1
                j += 1
        return max_count