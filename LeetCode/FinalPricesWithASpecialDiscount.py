from typing import List

def finalPrices(prices: List[int]) -> List[int]:
        # Monotonic increasing stack (?)
        stack = []
        n = len(prices)

        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                pop_idx = stack.pop()
                prices[pop_idx] -= prices[i]
            stack.append(i)
        return prices

p = [8,4,6,2,3]
print(finalPrices(p))