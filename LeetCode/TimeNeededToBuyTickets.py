from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Queue approach
        time = 0
        n = len(tickets)
        while tickets:
            time += 1
            tickets[0] -= 1
            if tickets[k] == 0: break

            if tickets[0] == 0:
                tickets.pop(0)
                n -= 1
            else:
                front = tickets.pop(0)
                tickets.append(front)

            if k == 0: k = n - 1
            else: k -= 1

        return time