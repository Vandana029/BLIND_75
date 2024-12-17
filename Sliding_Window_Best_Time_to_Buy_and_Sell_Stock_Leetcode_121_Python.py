class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers
        # Memory: O(1), only using two extra variables for pointers
        # Time: O(n), as we are traversing through list only one time
        left, right = 0, 1  # left: buy, right: sell
        max_profit = prices[right] - prices[left]
        while right < len(prices):
            curr_profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(curr_profit, max_profit)
            right += 1
        return max_profit
    
    
'''
Here's the intuition in plain words:

1. Start with the first day as your "buy" (left) and the next day as your "sell" (right).
2. Keep moving right forward to explore all possible selling days.
3. At each step:
    - If the price at right is lower than the price at left:
        - Move left to right because we found a new lowest buying price.
    - Otherwise, calculate the profit (prices[right] - prices[left]) and update the maximum profit if it's larger than the previous value.
4. Keep repeating until you reach the end of the list.
'''
