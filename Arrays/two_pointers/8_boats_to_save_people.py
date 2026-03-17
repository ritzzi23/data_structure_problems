"Always try to pair the heaviest person with the lightest person."
#Every person's weight is ≤ limit, 
#so everyone can always fit alone. 
#1 <= people[i] <= limit

from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1
        #left <= right because we want to check the 1 single person case as well
        while (left <= right):
            #if the sum of the two people is less than or equal to the limit, then we can pair them
            if people[left] + people[right] <= limit:
                left += 1
            #if the sum of the two people is greater than the limit, then we can only pair the heaviest person
            else:
                right -= 1
            #increment the count
            #even when a heavy person can't pair with a lighter person, 
            # we still need to increment the count because they will take up a boat
            count += 1
        return count
        
#Time Complexity: O(n log n)
#Space Complexity: O(1)