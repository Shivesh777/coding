# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays.

    Args:
        nums1 (List[int]): First sorted array.
        nums2 (List[int]): Second sorted array.

    Returns:
        float: Median of the two sorted arrays.

    Approach:
    - If len(nums1) > len(nums2), swap the arrays for uniform processing.
    - Initialize pointers 'left' and 'right' for binary search.
    - Calculate the total length 'N' of combined arrays.
    - Perform binary search:
        - Calculate partition indices 'A' and 'B' for nums1 and nums2.
        - Find values 'x1', 'y1', 'x2', and 'y2' for comparison.
        - Adjust pointers based on comparisons.
    - Return the median based on even or odd length.

    Complexity Analysis:
    - Time complexity: O(log(min(m, n))), where m and n are the lengths of 'nums1' and 'nums2'.
    - Space complexity: O(1).
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    N = m + n

    while left <= right:
        A = (left + right) // 2
        B = ((N + 1) // 2) - A

        x1 = -float("inf") if A - 1 < 0 else nums1[A - 1]
        y1 = float("inf") if A == m else nums1[A]
        x2 = -float("inf") if B - 1 < 0 else nums2[B - 1]
        y2 = float("inf") if B == n else nums2[B]

        if x1 <= y2 and x2 <= y1:
            if N % 2 == 0:
                return (max(x1, x2) + min(y1, y2)) / 2
            else:
                return max(x1, x2)
        elif x1 > y2:
            right = A - 1
        else:
            left = A + 1
