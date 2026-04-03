class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            n = nums[mid]
            print(f"{i = }, {j = }, {n = }")
            if n == target:
                return mid
            elif n < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1