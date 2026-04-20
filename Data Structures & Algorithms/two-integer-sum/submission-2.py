class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberDict = {}
        for i,v in enumerate(nums):
            toFind = target - v
            if toFind in numberDict:
                return [numberDict[toFind], i]
            numberDict[v] = i
