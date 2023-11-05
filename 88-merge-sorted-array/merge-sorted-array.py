from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays 'nums1' and 'nums2' in-place. The merged result is stored in 'nums1'.

        Args:
            nums1 (List[int]): The first sorted array with space for merged elements.
            m (int): The number of elements in 'nums1'.
            nums2 (List[int]): The second sorted array.
            n (int): The number of elements in 'nums2'.

        Returns:
            None
        """
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1.
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        