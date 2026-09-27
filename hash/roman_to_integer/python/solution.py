class Solution:
    def romanToInt(self, s: str) -> int:
        mapping: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # > "III" = 3
        result = 0
        splited_ss = list(s)

        for index, splited_s in enumerate(splited_ss):
            value = mapping[splited_s]
            # print("~~", (len(splited_ss) - 1), index, (len(splited_ss) - 1) > index)
            next_splited_s: None | str = (
                splited_ss[index + 1] if (len(splited_ss) - 1) > index else None
            )
            if next_splited_s is None:
                result += value
                continue

            next_value = mapping.get(next_splited_s)
            # print("~", next_value)
            if next_value is None:
                continue
            print(result, value, next_value)
            if value > next_value:
                result += next_value - value
                continue

            result += value

            # print(index)
            # if index != 0:
            #     prev_s = splited_ss[index - 1]
            #     print("if", prev_s, splited_s, result)
            #     if splited_s == prev_s:
            #         value = mapping.get(splited_s)
            #         if value:
            #             result += value
            #     else:
            #         value = mapping.get(splited_s)
            #         prev_value = mapping.get(prev_s)
            #         if value and prev_value:
            #             if prev_value < value:
            #                 result += abs(prev_value - value)
            #             else:
            #                 result += value
            # elif (index + 1) < len(splited_ss):
            #     next_s = splited_ss[index + 1]
            #     print("elif", splited_s, next_s, result)
            #     if splited_s == next_s:
            #         value = mapping.get(splited_s)
            #         if value:
            #             result += value
            #     else:
            #         value = mapping.get(splited_s)
            #         next_value = mapping.get(next_s)
            #         if value and next_value:
            #             if next_value > value:
            #                 result += next_value - value
            #             else:
            #                 result += value
            # else:
            #     print("else")
            #     value = mapping.get(splited_s)
            #     if value:
            #         result += value

            # print("if", (index + 1), len(splited_ss), " result:", result)
            # if (index + 1) < len(splited_ss):
            #     next_s = splited_ss[index + 1]
            #     if splited_s == next_s:
            #         value = mapping.get(splited_s)
            #         if value:
            #             result += value
            #     else:
            #         value = mapping.get(splited_s)
            #         next_value = mapping.get(next_s)
            #         if value and next_value:
            #             if next_value > value:
            #                 result += next_value - value
            #             else:
            #                 result += value
            # else:
            #     value = mapping.get(splited_s)
            #     if value:
            #         result += value

        return result


s = Solution()
# print(s.romanToInt(s="III"))
# print(s.romanToInt(s="LVIII"))
print(s.romanToInt(s="I"))
print(s.romanToInt(s="II"))
print(s.romanToInt(s="III"))
print(s.romanToInt(s="IV"))
