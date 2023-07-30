def find132pattern(nums):
    stack = []
    third = float('-inf')

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])

    return False

# Test examples
nums1 = [1, 2, 3, 4]
print(find132pattern(nums1))  # Output: False

nums2 = [3, 1, 4, 2]
print(find132pattern(nums2))  # Output: True

nums3 = [-1, 3, 2, 0]
print(find132pattern(nums3))  # Output: True
