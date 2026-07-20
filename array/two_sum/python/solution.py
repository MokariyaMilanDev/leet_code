from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        difDict: dict[int, int] = {}

        for rowIndex, rowNum in enumerate(iterable=nums):
            diffNum = target - rowNum
            if diffNum in difDict:
                return [difDict[diffNum], rowIndex]
            difDict[rowNum] = rowIndex

        return []


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
