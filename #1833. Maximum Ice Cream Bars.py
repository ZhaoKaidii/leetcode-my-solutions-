class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=False)
        y=0
        for i in range(len(costs)):
            if coins>=costs[i]:
                coins=coins-costs[i]
                y=y+1
            else: 
                break
        return y
