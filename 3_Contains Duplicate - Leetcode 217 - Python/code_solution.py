class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        # 1: Brute
        # Time: O(n^2), Space: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                #print(i, j, end=' # ')
                if nums[i] == nums[j]:
                    return True
        return False
        '''

        '''
        # 2.1: Medium
        # Time: O(nlogn), Space: O(n)
        sorted_list = sorted(nums)
        #print(sorted_list)
        n = len(nums) 
        for i in range(n-1):
            if sorted_list[i] == sorted_list[i+1]:
                return True
        return False
        '''

        '''
        # 2.2: Medium
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        #print(nums)
        n = len(nums) 
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        '''

        '''
        3: Optimal 
        Trick: Trade time with space and think suitable data structure to hold the critical information
        Time: O(n), Space: O(n)

        === My Learning from this question ===
        1. We are using hash table bcz insertion and lookup, both are O(1)
        2. Both dictionaries and sets in Python are implemented using hash tables. 
        3. 'in' operator returns True if the key exists in the dictionary

        hash_table = set() 
        for num in nums:
            if num in hash_table: 
                return True
            else:
                hash_table.add(num)
        return False 
        '''
        
        # Pythonic way
        n = set(nums)
        # print(list(n), nums)
        if len(n) == len(nums):
            return False
        return True


        