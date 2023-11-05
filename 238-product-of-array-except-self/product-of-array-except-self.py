from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate the product of all elements in the array except the current element.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: The list of products for each element.
        """
        n = len(nums)
        
        # Initialize two arrays for the left and right products
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate the left products for each element
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate the right products for each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Calculate the result array by multiplying left and right products
        result = [left_products[i] * right_products[i] for i in range(n)]
        
        return result

        