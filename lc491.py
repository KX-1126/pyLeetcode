from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(nums, startIndex):
            nonlocal path
            if startIndex == len(nums):
                return

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                if isIncrementalArray(path):
                    result.append(path[:])
                # result.append(path[:])
                backtracking(nums, i + 1)
                path.pop()

        def isIncrementalArray(nums):
            if len(nums) < 2:
                return False
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True

        backtracking(nums, 0)
        return result

so = Solution()
input1 = [4,4,3,2,1]

res = so.findSubsequences(input1)
print(res)

