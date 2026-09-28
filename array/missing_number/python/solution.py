class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        tt: set = set(nums)
        for i in range(0, len(tt)):
            value = nums[i]
            next_value = value + 1
            # print(
            #     "i=",
            #     i,
            #     " | value=",
            #     value,
            #     " | next=",
            #     next_value,
            #     " | !=",
            #     value + 1 != next_value,
            # )
            if next_value not in nums:
                return next_value
        return -1


s = Solution()
nums = [9, 6, 6, 6, 6, 4, 2, 3, 5, 7, 0, 1]  # -> 8
# [0, 1] -> 2
# [3, 0, 1] -> 2
print(s.missingNumber(nums=nums))
