class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # use prefix products
        prefix_product = 1
        for i in range(len(nums) - 1):
            prefix_product *= nums[i]
            output[i + 1] *= prefix_product

        # use suffix products
        suffix_product = 1
        for i in range(len(nums) - 1, 0, -1):
            suffix_product *= nums[i]
            output[i - 1] *= suffix_product
        
        return output