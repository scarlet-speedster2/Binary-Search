import random
def right_boundary_included(nums,target):

    if not nums:
        return -1
    left = 0
    right = len(nums) - 1

    #case [left,right]
    while left <= right:

        mid = left + (right - left) //2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1 if right < 0 or nums[right] != target else right
def right_boundary(nums,target):

    if not nums:
        return -1

    left = 0
    right = len(nums)

    #case [left,right)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

    return left - 1

l = [random.randint(0,10) for x in range(100)]
l.sort()
print(l)

x = int(input('Enter search element '))
print(right_boundary_included(l,x))