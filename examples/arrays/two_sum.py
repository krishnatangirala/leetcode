class Solution:
    """
    LeetCode Problem #1: Two Sum
    [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # --- SOLUTION IMPLEMENTATION ---
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
        # -----------------------------

# This block only runs when you execute the file directly (python array/two_sum.py)
if __name__ == "__main__":
    # 1. Instantiate the Solution class
    solver = Solution()

    # 2. Define your test cases (input and expected output)

    # Test Case 1: Standard case
    nums1, target1 = [2, 7, 11, 15], 9
    expected1 = [0, 1]
    result1 = solver.twoSum(nums1, target1)

    # Test Case 2: Different order/negative numbers
    nums2, target2 = [3, 2, 4], 6
    expected2 = [1, 2] # or [2, 1], depending on implementation
    result2 = solver.twoSum(nums2, target2)

    # 3. Print the results for verification
    print()
    print(f"--- Running Two Sum Tests ---")

    # Simple check for Test 1
    print(f"Case 1 (Target: {target1}):")
    print(f"  Input: {nums1}")
    print(f"  Expected: {expected1}")
    # Note: Python lists are mutable, so we sort the results to ensure order doesn't matter for the check
    print(f"  Result: {result1} -> {'PASS' if sorted(result1) == sorted(expected1) else 'FAIL'}")

    # Simple check for Test 2
    print(f"Case 2 (Target: {target2}):")
    print(f"  Input: {nums2}")
    print(f"  Expected: [1, 2] or [2, 1]")
    print(f"  Result: {result2} -> {'PASS' if sorted(result2) == sorted(expected2) else 'FAIL'}")