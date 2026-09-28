class Solution:
    def recoverOrder(self, orders: list[int], friends: list[int]) -> list[int]:
        result = []
        for order in orders:
            if order in friends:
                result.append(order)
        return result


s = Solution()
order = [1, 4, 5, 3, 2]
friends = [2, 5]
print(s.recoverOrder(orders=order, friends=friends))
# > OUTPUT = [5,2]
# order = [3, 1, 2, 5, 4]
# friends = [1, 3, 4]
# OUTPUT = [3,1,4]
