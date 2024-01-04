# Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find indices of two numbers in an array that sum up to the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum of two numbers.

    Returns:
        List[int]: Indices of the two numbers that add up to the target.

    Approach:
    - Use a dictionary 'seen' to track numbers traversed along with their indices.
    - For each number x in 'nums':
        - Calculate the difference 'diff' between 'target' and 'x'.
        - If 'diff' exists in 'seen', return its index and current index 'i'.
        - Otherwise, add 'x' to 'seen' with its index 'i'.
    - If no pair found, return an empty list.

    Complexity Analysis:
    - Time complexity: O(n), where n is the length of 'nums'.
    - Space complexity: O(n) for the dictionary 'seen'.
    """
    seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """
    Find indices of two numbers in an array that sum up to the target using a brute force approach.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum of two numbers.

    Returns:
        List[int]: Indices of the two numbers that add up to the target.

    Approach:
    - Iterate through each element 'i' in 'nums'.
    - For each 'i', iterate through all subsequent elements 'j' in 'nums'.
    - Check if 'nums[i] + nums[j]' equals 'target'.
    - If found, return the indices 'i' and 'j'.
    - If no pair found, return an empty list.

    Complexity Analysis:
    - Time complexity: O(n^2), where n is the length of 'nums'.
    - Space complexity: O(1), no extra space used apart from the input.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Return empty list if no pair found
