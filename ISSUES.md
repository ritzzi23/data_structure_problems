# Repository Issues

## Critical Bugs

### Graphs
1. **graphs/problems_bfs_dfs/island_perimeter.py:29** — `grid[nx][nx] = -1` should be `grid[nx][ny] = -1` (wrong index)
2. **graphs/practice_problems_bfs_dfs/5_island_perimeter.py:38** — Same `grid[nx][nx]` bug (duplicate file)
3. **graphs/problems_bfs_dfs/max_area_of_island.py:16** — `while queue:` loop is indented inside an `if`, so BFS doesn't process full islands
4. **graphs/bfs.py:8** — `bfs_recursive()` calls itself without checking if queue is empty → infinite recursion
5. **graphs/practice_problems_bfs_dfs/1_number_of_provinces.py:25** — `visited` list sized from `defaultdict` length instead of `n` → potential IndexError

### Linked List
6. **linked_list/6_add_two_numbers.py:15** — Returns `[0]` (a list) instead of `ListNode(0)`
7. **linked_list/add_two_numbers.py:12** — Same wrong return type `[0]`
8. **linked_list/add_two_numbers_ii.py:21** — Same wrong return type `[0]`

### Dynamic Programming
9. **dynamic_programming/1D_DP/Kadane_algorithm/maximum_product_subarray.py:66** — `dp = [(0,0)] * (n+1)` shares the same tuple object across all indices (classic Python gotcha). Should use a list comprehension.
10. **dynamic_programming/21_Longest_Common_Subsequence/25_shortest_common_supersequence.py:64** — `dp = [[[""] for ...]]` has an extra list wrapper; should be `dp = [["" for ...]]`
11. **dynamic_programming/9_partition_equal_subset_sum.py:117** — `1 << len(nums)` should be `1 << len(left)` (generates subsets for wrong array in meet-in-middle)
12. **dynamic_programming/1D_DP/7_0_1_knapsack/9_mitm_partition_equal_subset_sum.py:30** — Same `1 << len(nums)` bug
13. **dynamic_programming/1D_DP/7_0_1_knapsack/10_count_of_subset_with_given_sum.py:117** — Same `1 << len(nums)` bug

### Stacks
14. **Stacks/Part_3_monotonic_stack_&_queue_problems/1_next_greater_element_i.py:47-53** — Return statement and result-building code are at module level instead of inside the method

### Old Trees
15. **old_trees/binary_tree_inorder_traversal.py:95** — Calls undefined method `inorderTraversal()` (should be `inorderTraversal_recursive()` or `_iterative()`)
16. **old_trees/boundary_of_binary_tree.py:116** — Variable `right` used before it's defined → NameError

### Binary Search
17. **binary_search/find_peak_element.py:25** — Returns hardcoded `1` when `mid == 0` without validating it's a peak
18. **binary_search/find_the_peaks.py:6** — Returns `[0]` for length-1 array; single element can't be a peak
19. **binary_search/2_binary_search_on_rotated_sorted_array/1_find_minimum_in_rotated_sorted_array.py:26** — Missing return after while loop exits
20. **binary_search/binary_search_on_answers/part2_median_of_two_sorted_arrays.py:38** — Missing return statement if loop exits without finding partitions

### Arrays / Sliding Window
21. **Arrays/sliding_window/variable_window/longest_substring_without_repeating_characters.py:19** — Missing `j += 1` after shrinking window → potential infinite loop
22. **Arrays/sliding_window/variable_window/longest_substring_with_k_uniques.py:26** — Same missing `j += 1` → infinite loop

### Design
23. **Design/5_design_hashMap.py:36** — `remove()` returns `-1` instead of `None`

---

## Incomplete / Empty Files
- **Arrays/two_pointers/4_4Sum.py** — docstring only
- **Arrays/Prefix_suffix_arrays/1_trapping_rain_water.py** — comment only
- **Arrays/Sorting/1_sort_an_array.py** — comment only
- **Arrays/Sorting/2_top_k_frequent_elements.py** — empty function
- **Arrays/Sorting/dutch_national_flag_algorithm/1_sort_colors.py** — empty
- **dynamic_programming/1D_DP/Kadane_algorithm/maximum_sum_circular_subarray.py** — incomplete
- **dynamic_programming/1D_DP/Kadane_algorithm/divide_conquer_maximum_subarray.py** — comment only
- **dynamic_programming/1D_DP/14_unbounded_knapsack/17_coin_change_ii.py** — empty
