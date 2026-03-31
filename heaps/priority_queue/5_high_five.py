#Total Time Complexity: O(n log n)
#Space Complexity: O(n)
#Brute Force
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(list) #Space Complexity: O(n)

        for id, score in items: #Time Complexity: O(n)
            hash_map[id].append(score)

        result = [] #Space Complexity: O(n)
        for i,v in hash_map.items(): #Time Complexity: O(n)
            v.sort(reverse = True) #Time Complexity: O(n log n)
            total = 0
            for k in range(5):
                total += v[k]
            total = total//5 #floor division (used when we need to round down)(no decimals needed)
            result.append((i,total))
        result.sort(key=lambda x:x[0])
        return result

#-----------------------------------------------------------------------------------

#Optimal Solution (heap)

import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(list)  # Space Complexity: O(m)

        for id, score in items:  # Total loop runs n times
            heapq.heappush(hash_map[id], score)  # Time Complexity: O(log 5) = O(1)
            if len(hash_map[id]) > 5:  # Time Complexity: O(1)
                heapq.heappop(hash_map[id])  # Time Complexity: O(log 5) = O(1)

        result = []  # Space Complexity: O(m)

        for i, v in hash_map.items():  # Time Complexity: O(m)
            total = 0
            for k in range(5):  # Time Complexity: O(1)
                total += v[k]
            total = total // 5
            result.append([i, total])

        result.sort(key=lambda x: x[0])  # Time Complexity: O(m log m)
        return result

#--------------------------------
#https://enginebogie.com/public/question/calculate-maximum-average-score/1925
#Time Complexity: O(n)
#Space Complexity: O(n)
def max_average_score(scores):
    hash_map = {}
    for name, score in scores:
        if name not in hash_map:
            hash_map[name] = []
        hash_map[name].append(int(score))
    
    max_avg = float('-inf')
    for name in hash_map:
        avg = sum(hash_map[name]) / len(hash_map[name])
        if avg > max_avg:
            max_avg = avg
    
    return max_avg