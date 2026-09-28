# > Two pointer approach
# > i and j
# > i = index
# > j = i + 1


class Solution:
    def remove_duplicate(self, nums: list[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            # print("j=", j, " | i=", i, " | nums[i]=", nums[i], " | nums[j]=", nums[j])
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


s = Solution()
nums = [1, 1, 1, 2, 2, 3, 3, 3]
print(s.remove_duplicate(nums=nums))
print("nums ", nums)
