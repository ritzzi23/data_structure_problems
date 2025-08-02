# Data Structure and Algorithm Problems

A comprehensive collection of data structure and algorithm problems implemented in Python. This repository contains solutions to various coding problems organized by categories.

## 📁 Repository Structure

### Binary Search
- **Classic Binary Search**: Basic binary search implementations
- **Rotated Sorted Arrays**: Search in rotated arrays, find minimum
- **Peak Binary Search**: Find peak elements
- **Binary Search on Answers**: Square root, median of sorted arrays

### Dynamic Programming
- **0/1 Knapsack**: Classic knapsack problems and variations
- **1D DP**: 
  - Basic problems: Fibonacci, climbing stairs, house robber, frog jump
  - **Kadane's Algorithm**: Maximum subarray problems
  - **Longest Increasing Subsequence**: LIS with O(n²) and O(n log n) solutions
  - Unbounded knapsack problems
- **Longest Common Subsequence**: LCS problems and variations
- **Matrix Chain Multiplication**: Dynamic programming for matrix operations
- **Unbounded Knapsack**: Coin change and rod cutting problems

### Graphs
- **BFS/DFS**: Breadth-first and depth-first search implementations
- **Cycle Detection**: Detect cycles in directed and undirected graphs
- **Shortest Paths**: Dijkstra's, Bellman-Ford algorithms
- **Minimum Spanning Tree**: Prim's and Kruskal's algorithms
- **Topological Sort**: Kahn's algorithm and DFS-based approach
- **Connected Components**: Island problems and graph connectivity

### Heaps
- **Binary Heap**: Implementation from scratch
- **Heap Operations**: Insert, delete, heapify
- **Heap Sort**: Sorting using heap data structure

### Linked Lists
- **Basic Operations**: Reverse, add two numbers
- **Advanced Problems**: Add two numbers II, reverse doubly linked list

### Sliding Window
- **Fixed Window**: Maximum sum of distinct subarrays
- **Variable Window**: Longest substring problems, minimum size subarray

### Strings
- **String Manipulation**: Anagrams, isomorphic strings, rotations
- **Pattern Matching**: KMP algorithm
- **Character Frequency**: Sort by frequency

### Trie
- **Prefix Tree**: Basic trie implementation
- **Advanced Trie**: Trie with count operations

### Bit Manipulation
- **Power Operations**: Power of two, power set
- **Bit Operations**: Check if bit is set

## 🚀 Getting Started

### Prerequisites
- Python 3.7+

### Running Problems
Each problem is self-contained and can be run independently. For example:

```bash
python dynamic_programming/1D_DP/32_longest_increasing_subsequence/32_longest_increasing_subsequence.py
```

## 📚 Problem Sources
- LeetCode
- GeeksforGeeks
- Aditya Verma Dynamic Programming Series
- Various coding competitions

## 🧮 Algorithm Categories

### Time Complexity Analysis
- **Binary Search**: O(log n)
- **Dynamic Programming**: O(n²) to O(n³) depending on problem
- **Graph Algorithms**: O(V + E) for BFS/DFS, O(V²) for dense graphs
- **Heap Operations**: O(log n) for insert/delete, O(n) for heapify
- **String Algorithms**: O(n) to O(n²) depending on algorithm

### Space Complexity Analysis
- **Most DP problems**: O(n²) for 2D DP tables
- **1D DP problems**: O(n) for 1D DP tables
- **Graph algorithms**: O(V) for visited arrays, O(V²) for adjacency matrices
- **Heap**: O(n) for storage
- **Trie**: O(ALPHABET_SIZE * n * m) where n is number of words, m is average length

## 🎯 Key Algorithms Implemented

1. **Binary Search Variations**
   - Classic binary search
   - Search in rotated sorted arrays
   - Find peak elements
   - Binary search on answer space

2. **Dynamic Programming Patterns**
   - **1D DP Problems**:
     - 0/1 Knapsack
     - Unbounded Knapsack
     - Longest Common Subsequence
     - Matrix Chain Multiplication
     - **Kadane's Algorithm** (Maximum Subarray)
     - **Longest Increasing Subsequence**
   - **2D DP Problems**:
     - Longest Common Subsequence
     - Matrix Chain Multiplication

3. **Graph Algorithms**
   - BFS and DFS
   - Cycle Detection
   - Shortest Path (Dijkstra, Bellman-Ford)
   - Minimum Spanning Tree (Prim, Kruskal)
   - Topological Sort

4. **Data Structures**
   - Binary Heap
   - Trie (Prefix Tree)
   - Linked Lists

## 📝 Contributing

Feel free to contribute by:
- Adding new problem solutions
- Improving existing solutions
- Adding better documentation
- Optimizing algorithms


## 🔗 Useful Resources

- [LeetCode](https://leetcode.com/)
- [GeeksforGeeks](https://www.geeksforGeeks.org/)
- [Aditya Verma Dynamic Programming Playlist](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)

---

**Happy Coding! 🚀** 