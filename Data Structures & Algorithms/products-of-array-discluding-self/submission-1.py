class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Get prefix products
        prefixProduct = 1
        for i in range(len(nums) - 1):
            prefixProduct *= nums[i]
            result[i + 1] *= prefixProduct

        # Get suffix products
        suffixProduct = 1
        for i in range(len(nums) - 1, 0, -1):
            suffixProduct *= nums[i]
            result[i - 1] *= suffixProduct

        return result