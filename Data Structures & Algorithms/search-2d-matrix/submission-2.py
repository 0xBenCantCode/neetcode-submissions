class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            upper = len(i) - 1
            lower = 0
            
            while lower <= upper:

                middle = (upper + lower) // 2

                if i[middle] == target:
                    return True

                if i[middle] < target:
                    lower = middle + 1

                if i[middle] > target:
                    upper = middle - 1
        return False




        