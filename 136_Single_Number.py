# Griffin Wong
# 03/27/2020
# Drexel University

'''
Given a non-empty array of integers, 
every element appears twice except for one. 
Find that single one.

NOTE:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
'''

class Solution: # Function Definition
    def singleNumber(self, nums: List[int]) -> int:
        
        list_one = [] # Empty list to add non-duplicates
        list_two = [] # Empty list to add duplicates
        list_three = [] # Empty list to add single-elements

        # Check for duplicates within the given list
        for i in nums: 
            if i not in list_one:
                list_one.append(i)
            else:
                list_two.append(i)

        # Compare the two lists
        for i in list_one:
            for j in list_two:
                if i != j:
                    list_three.append(i)
    
        # Print the single element
        for i in list_three:
            return(i)