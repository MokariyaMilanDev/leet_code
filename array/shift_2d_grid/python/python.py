from typing import List

# > [["A", "B"], ["C", "D"], ["E", "F"]] 2
# ? [[0, 1], [2, 3], [4, 5]]

# > [["B", "C"], ["D", "E"], ["F", "A"]] 1

# > [["C", "D"], ["E", "F"], ["A", "B"]] 0


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatGrid = [item for sublist in grid for item in sublist]
        k = k % len(flatGrid)
        targetCells = flatGrid[-k:]
        targetCells.extend(flatGrid[:-k])

        result: List[List[int]] = []
        index = 0
        for rowIndex, row in enumerate(grid):
            result.append([])
            for colIndex, col in enumerate(row):
                result[rowIndex].append(targetCells[index])
                index += 1

        return result


s = Solution()
# print(s.shiftGrid(grid=[[0, 1], [2, 3], [4, 5]], k=3))
print(s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
# print(s.shiftGrid(grid=[[1], [2], [3], [4], [7], [6], [5]], k=23))
