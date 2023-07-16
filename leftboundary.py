

def left_with_range(nums,target):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1 if left >= len(nums) or nums[left] != target else left

def left_boundary(nums,target):

    if not nums:
        return -1


    left = 0
    right = len(nums)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

    return left

l = [x for x in range(100)]

x = int(input('Enter the search element'))

print(left_with_range(l,x))