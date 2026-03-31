'''
Time Complexity: O(d) where d is the number of distinct remainders before a repeat is found (or the remainder becomes 0). 
In the worst case, d can be up to denominator - 1, so O(denominator).
Space Complexity: O(d) for both the remainder_map and the result list, which store up to d entries each.
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #Edge Case 1
        if numerator == 0:
            return "0"
        result = []
        #Edge Case 2
        if numerator * denominator < 0:
            result.append("-")

        abs_numerator = abs(numerator)
        abs_denominator = abs(denominator)

        #Integer Part
        integer_part = abs_numerator // abs_denominator
        result.append(str(integer_part))

        #Fraction Part
        remain = abs_numerator % abs_denominator

        if remain == 0:
            return ("".join(result))

        result.append(".")

        remainder_map = {}

        while remain!= 0:
            #Check if the remainder is already in the map
            if remain in remainder_map:
                #If the remainder is already in the map, it means we have found a repeating decimal
                #As we are collection the length of the result at every step, we can use the length of the result to find the position of the repeating decimal
                insert_pos = remainder_map[remain]
                #Insert the opening parenthesis at the position of the repeating decimal
                result.insert(insert_pos,"(")
                #Insert the closing parenthesis at the end of the result
                result.append(")")
                break
            
            #if the remainder is not in the map, add it to the map
            #We store the length of the current resulting list at in the map with key as the remainder
            remainder_map[remain] = len(result)

            #Multiply the remainder by 10 to get the next digit
            remain *= 10
            #Get the next digit
            digit = remain // abs_denominator
            #Append the next digit to the result
            result.append(str(digit))
            #Get the next remainder
            remain %= abs_denominator

        return ("".join(result))

        