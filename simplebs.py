
def binarysearch(nums,target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binarys(nums,target):

    if not nums:
        return -1
    left = 0
    right = len(nums) - 1

    while left < right:

        mid = left + (right - left)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

    return left if nums[left] == target else -1


l = [int(x) for x in input().split()]

l.sort()
x = int(input("Enter search element"))
print(binarys(l,x))
