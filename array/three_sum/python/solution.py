#! Not Resolved


class Solution:
    def checkKeyExists(self, keys: list[str], record: dict[str, list[int]]) -> tuple:
        for key in keys:
            exists = record.get(key)
            if exists:
                return (True, key)
        else:
            return (False, None)

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        sorted_nums = sorted(nums)
        record: dict[str, list[int]] = {}
        print(sorted_nums)
        for _index, _num in enumerate(sorted_nums):
            for __index, __num in enumerate(sorted_nums):
                for ___index, ___num in enumerate(sorted_nums):
                    keys = [
                        f"{_index}{__index}{___index}",
                        f"{_index}{___index}{__index}",
                        f"{__index}{_index}{___index}",
                        f"{__index}{___index}{_index}",
                        f"{___index}{__index}{_index}",
                        f"{___index}{_index}{__index}",
                    ]
                    exists, key = self.checkKeyExists(keys=keys, record=record)

                    if (
                        _index != __index
                        and _index != ___index
                        and __index != ___index
                        and exists is None
                    ):
                        sum = _num + __num + ___num
                        if sum == 0:
                            pair: list[int] = [_num, __num, ___num]
                            record[key] = pair
                            result.append(pair)

        return result


s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # Output [[-1,-1,2],[-1,0,1]]
