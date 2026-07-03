class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        # result array will store the final answers
        result = [1] * n
        
        # keeps track of product of elements to the left
        left_product = 1
        
        for i in range(n):
            # store product of all elements before index i
            result[i] = left_product
            
            # update left product by multiplying current number
            left_product *= nums[i]
        
        # keeps track of product of elements to the right
        right_product = 1
        
        # loop from right to left
        for i in range(n - 1, -1, -1):
            # multiply current value with right side product
            result[i] *= right_product
            
            # update right product by multiplying current number
            right_product *= nums[i]
        
        return result