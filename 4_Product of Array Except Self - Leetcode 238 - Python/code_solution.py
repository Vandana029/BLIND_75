class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        # 1: Brute
        # Time: O(n^2), Space: O(n)

        #### ---- Very Slow, Time limit Exceeded ---- ####
        n = len(nums)
        ans = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    product *= nums[j] 
                    #print(i, j, end=' # ')
            ans.append(product)
        return ans
        '''

        '''
        # 2: Medium (This solution is invalid because it uses division which is not allowed as per the question)
        # Time: O(n), Space: O(1) bcz output space is not counted
        
        product = 1
        ans = []

        
        #### ---- Failing where list contains 0 ---- ####
        # for num in nums:
        #     product *= num

        # for num in nums:
        #     ans.append(product / num)

        # return ans
        

        count = sum(1 for x in nums if x == 0)

        if count >= 2:
            return [0] * len(nums)  # all element as zero
        elif count == 1: # only one 0 in list
            for num in nums:
                if num != 0:
                    product *= num

            for num in nums:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)

            return ans
        else:
            for num in nums:
                product *= num

            for num in nums:
                ans.append(int(product / num))

            return ans



        ### --- Debugging --- ####
        # x = nums.count(0) # Not working in Leetcode env
        # print(x==1)
        # count = sum(1 for x in nums if x == 0) # Working in Leetcode env
        # print(count)

        '''

        # 3. Optimal
        prefix, postfix = 1, 1
        n = len(nums)
        answer = [1] * n

        for i, num in enumerate(nums):
            # answer[i] *= prefix # this takes more time
            answer[i] = prefix # so, instead use this
            prefix *= num

        # for i in range(n):
        #     answer[n-i-1] *= postfix
        #     postfix *= nums[n-i-1] 

        # Pythonic way, which is also faster
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i] 
        
        return answer


        