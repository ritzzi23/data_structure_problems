# Data Structure and Algorithm Problems

A comprehensive collection of **261 data structure and algorithm problems** implemented in Python, organized by topic and pattern. Each solution includes multiple approaches — from brute force to optimized — with detailed time/space complexity analysis and dry runs.

## Repository Stats

| Metric | Value |
|---|---|
| **Total Problems** | 261 |
| **Language** | Python 3.7+ |
| **Topics Covered** | 18 |
| **Approach Style** | Recursive → Memoized → Tabulated → Space-Optimized |

## Repository Structure

### Arrays (34 problems)
| Sub-Topic | Problems |
|---|---|
| **Two Pointers** | Two Sum, Two Sum II, 3Sum, 4Sum, Container With Most Water, Trapping Rain Water, Is Subsequence, Boats to Save People, Remove Duplicates from Sorted Array |
| **Hashing** | Find Duplicates, Valid Anagram, Group Anagrams, Design HashSet, Design HashMap, Longest Consecutive Sequence, First Unique Character, Fraction to Recurring Decimal, Find Most Occurring IP Address |
| **Sliding Window (Fixed)** | Maximum Sum of Distinct Subarrays with Length K, Sliding Window Maximum |
| **Sliding Window (Variable)** | Longest Substring with At Most K Distinct Characters, Longest Substring Without Repeating Characters, Longest Repeating Character Replacement, Minimum Size Subarray Sum, Minimum Window Substring |
| **Prefix/Suffix Arrays** | Trapping Rain Water |
| **Sorting** | Sort an Array, Top K Frequent Elements, Encode and Decode Strings, Dutch National Flag (Sort Colors) |
| **Matrix** | Search a 2D Matrix, Search a 2D Matrix II |

### Binary Search (22 problems)
| Sub-Topic | Problems |
|---|---|
| **Classic Binary Search** | Bisect / Search Insert Position, Search in Sorted Array, Count Occurrences in Sorted Array, First and Last Position of Element, Implement Lower Bound, Implement Upper Bound |
| **Rotated Sorted Arrays** | Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array |
| **Peak Binary Search** | Find Peak Element, Find the Peaks |
| **Binary Search on Answers** | Square Root of a Number, Square Root to N Decimal Places, Median of Two Sorted Arrays (3 approaches), Kth Element of Two Sorted Arrays |

### Dynamic Programming (35 problems)
| Sub-Topic | Problems |
|---|---|
| **1D DP** | Fibonacci Number, Climbing Stairs, Min Cost Climbing Stairs, Frog Jump, Frog Jump with K Distances (Forward + Back approach), House Robber I & II |
| **Kadane's Algorithm** | Maximum Subarray, Maximum Product Subarray, Maximum Sum Circular Subarray, Divide & Conquer Maximum Subarray |
| **0/1 Knapsack** | 0/1 Knapsack Problem, Subset Sum Problem, Partition Equal Subset Sum (DP + Meet-in-the-Middle), Count of Subsets with Given Sum, Subset Sum Closest to Target, Partition Array to Minimize Sum Difference, Ones and Zeroes |
| **Unbounded Knapsack** | Knapsack with Duplicate Items, Minimum Cost to Cut a Stick, Coin Change, Coin Change II |
| **Longest Common Subsequence** | LCS, Longest Common Substring, Print LCS, Shortest Common Supersequence, Min Insertions/Deletions to Convert String, Longest Palindromic Subsequence, Minimum Insertion Steps to Make Palindrome, Longest Repeating Subsequence |
| **Longest Increasing Subsequence** | LIS with O(n²) and O(n log n) solutions |
| **Matrix Chain Multiplication** | MCM and variations |
| **DP on Stocks** | Best Time to Buy and Sell Stock |

### Graphs (68 problems)
| Sub-Topic | Problems |
|---|---|
| **BFS/DFS Fundamentals** | Adjacency List BFS (Iterative & Recursive), Adjacency List DFS (Iterative & Recursive) |
| **BFS/DFS Practice** | Number of Islands (BFS & DFS), Number of Provinces, Connected Components, Clone Graph, Flood Fill, Island Perimeter, Max Area of Island, 01 Matrix, Word Ladder, Is Graph Bipartite, Shortest Path in Binary Matrix |
| **Multi-Source BFS** | Rotting Oranges, Walls and Gates, Flood Fill |
| **Cycle Detection** | Undirected Graph Cycle (BFS & DFS), Directed Graph Cycle (BFS & DFS), Graph Valid Tree, Redundant Connection |
| **Topological Sort** | Kahn's Algorithm (BFS), DFS-based Topological Sort, Course Schedule I / II / IV, Alien Dictionary, Find Eventual Safe States (BFS & DFS) |
| **Shortest Path Algorithms** | Dijkstra's (3 implementations: basic, heap, heapq), Bellman-Ford (directed & undirected), Shortest Path in DAG, Network Delay Time |
| **Minimum Spanning Tree** | Prim's Algorithm, Kruskal's Algorithm (using DSU) |
| **Disjoint Set Union** | Union-Find Implementation, Cycle Detection with DSU, Connected Components, Graph Valid Tree, Find Root of Largest Tree in Forest |

### Heaps (8 problems)
| Sub-Topic | Problems |
|---|---|
| **Core Implementation** | Binary Min Heap from Scratch, Heap Operations (Insert, Delete, Heapify), Heap Sort |
| **Priority Queue** | Kth Largest Element in a Stream, Last Stone Weight, Kth Largest Element in an Array, Find Median from Data Stream, High Five |

### Stacks (14 problems)
| Sub-Topic | Problems |
|---|---|
| **Implementations** | Stack using Arrays, Stack using Queues, Queue using Stacks, Stack using Linked List |
| **Basic Problems** | Valid Parentheses, Min Stack |
| **Infix/Postfix** | Infix to Postfix Conversion |
| **Monotonic Stack** | Next Greater Element I & II, Next Smaller Element, Trapping Rain Water, Sum of Subarray Minimums, Asteroid Collision |
| **Monotonic Deque** | Sliding Window Maximum |

### Linked Lists (14 problems)
| Sub-Topic | Problems |
|---|---|
| **Basic Operations** | Reverse Linked List (Singly & Doubly), Merge Two Sorted Lists, Cycle Detection, Reorder List |
| **Advanced** | Add Two Numbers I & II, Remove Nth Node from End, Reverse Nodes in K-Group, Reverse Linked List II, Find the Duplicate Number |
| **Design** | Merge K Sorted Lists, Design Circular Queue |

### Trees (32 problems)
| Sub-Topic | Problems |
|---|---|
| **Traversals** | Inorder, Preorder, Postorder (Recursive & Iterative), Level Order I & II, Right Side View |
| **Primary Concepts** | Height of Tree |
| **DFS** | Balanced Binary Tree |
| **BST** | Convert Sorted Array to BST, Convert Sorted List to BST, Validate BST |
| **Classic Problems** | Invert Binary Tree, Maximum Depth, Diameter, Path Sum I & II, Same Tree, Lowest Common Ancestor, Maximum Path Sum, Completeness Check, Boundary Traversal, Vertical Order Traversal, Bottom View, Construct from Inorder + Preorder/Postorder, Amount of Time for Binary Tree to Be Infected |

### Strings (13 problems)
String Compression, First Unique Character, Longest Common Prefix, Isomorphic Strings, Rotate String, Longest Prefix Suffix, KMP Algorithm, Valid Anagram, Sort Characters by Frequency, Roman to Integer, Reverse Words in a String, Largest Odd Number in String, Regex Pattern

### Intervals (5 problems)
Insert Interval (For Loop & While Loop approaches), Merge Intervals, Non-Overlapping Intervals, Meeting Rooms

### Design (5 problems)
Design Circular Queue, LRU Cache, LFU Cache, Design HashSet, Design HashMap

### Trie (3 problems)
Implement Trie (Prefix Tree), Implement Trie II (with Count Operations), Longest Common Prefix using Trie

### Bit Manipulation (3 problems)
Power of Two, Power Set, Check if i-th Bit is Set

### Recursion (1 problem)
Josephus Problem (Find the Winner of the Circular Game)

### Sorting (1 problem)
Merge Sort

### Math (1 problem)
Reverse Integer

### In-Built Functions (2 files)
List Pop, List Remove

## Solution Approach

Each problem follows a consistent structure:

1. **Pattern Identification** — Classify the problem (Two Pointers, Sliding Window, DP, etc.)
2. **Multiple Approaches** — Brute force → Optimized, with clear progression
3. **Complexity Analysis** — Time and space complexity for every approach
4. **Dry Runs** — Step-by-step execution traces
5. **Edge Cases** — Boundary conditions and special inputs

For Dynamic Programming problems specifically, solutions progress through:
```
Recursion → Memoization (Top-Down) → Tabulation (Bottom-Up) → Space Optimization
```

## Getting Started

### Prerequisites
- Python 3.7+

### Running Problems
Each problem is self-contained and can be run independently:

```bash
python3 dynamic_programming/7_dp_on_subsequences/7_0_1_knapsack/7_0_1_knapsack_problem.py
```

### Project Structure
```
data_structure_problems/
├── Arrays/                          # 34 problems
│   ├── two_pointers/
│   ├── hashing/
│   ├── sliding_window/
│   │   ├── fixed_window/
│   │   └── variable_window/
│   ├── Prefix_suffix_arrays/
│   ├── Sorting/
│   │   └── dutch_national_flag_algorithm/
│   └── matrix_array/
├── binary_search/                   # 22 problems
│   ├── 1_classic_binary_search_on_sorted_array/
│   ├── 2_binary_search_on_rotated_sorted_array/
│   ├── 3_peak_binary_search/
│   └── binary_search_on_answers/
├── dynamic_programming/             # 35 problems
│   ├── 1D_DP/
│   │   └── Kadane_algorithm/
│   ├── 7_dp_on_subsequences/
│   │   ├── 7_0_1_knapsack/
│   │   └── 14_unbounded_knapsack/
│   ├── 21_Longest_Common_Subsequence/
│   ├── 32_longest_increasing_subsequence/
│   ├── 40_matrix_chain_multiplication/
│   └── DP_on_stocks/
├── graphs/                          # 68 problems
│   ├── practice_problems_bfs_dfs/
│   ├── problems_bfs_dfs/
│   │   └── multi_source_bfs/
│   ├── practice_problems_dsu/
│   ├── practice_problems_shortest_distance/
│   ├── practice_topo_sort/
│   └── undirected_cycle/
├── heaps/                           # 8 problems
│   └── priority_queue/
├── Stacks/                          # 14 problems
│   ├── Part_1/
│   ├── Part_2/
│   └── Part_3_monotonic_stack_&_queue_problems/
│       ├── monotonic_stack/
│       └── monotonic_deque/
├── linked_list/                     # 14 problems
├── trees/                           # 8 problems (+ 24 in old_trees/)
│   ├── traversals/
│   ├── primary_concepts/
│   └── DFS/
├── strings/                         # 13 problems
├── Intervals/                       # 5 problems
├── Design/                          # 5 problems
├── Trie/                            # 3 problems
├── bit_manipulation/                # 3 problems
├── recursion/                       # 1 problem
├── sorting/                         # 1 problem
├── math/                            # 1 problem
└── in_built_functions/              # 2 files
```

## Known Issues

See [ISSUES.md](ISSUES.md) for a list of known bugs and incomplete files that need attention.

## Problem Sources
- [LeetCode](https://leetcode.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [Aditya Verma Dynamic Programming Playlist](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- Various coding competitions

## License

This repository is for personal learning and reference purposes.
