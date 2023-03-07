from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        result.append(path)

        def backtracking(nums,startIndex):
            nonlocal path
            if startIndex == len(nums):
                return

            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                result.append(path[:])
                backtracking(nums,i+1)
                path.pop()

        nums.sort()
        backtracking(nums,0)
        return result

so = Solution()
input1 = [1,2,2]

res = so.subsetsWithDup(input1)
print(res)