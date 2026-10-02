class Solution:
    def equivalent(self, array1: list[str], array2: list[str]) -> bool:
        w1r = 0
        w1c = 0
        w2r = 0
        w2c = 0

        while len(array1) < w1r and len(array2) < w2r:
            print("> ", array1[w1r][w1c], array2[w2r][w2c])
            if array1[w1r][w1c] != array2[w2r][w2c]:
                return False

            if len(array1[w1r]) >= w1r:
                w1r += 1

            if len(array2[w2r]) >= w2r:
                w2r += 1

            w1c += 1
            w2c += 1

        return True


word1 = ["ab", "c"]
word2 = ["a", "bc"]

s = Solution()
is_same = s.equivalent(array1=word1, array2=word2)
print("Yes" if is_same else "No")
