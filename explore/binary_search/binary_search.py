class Solution:
    # Determine midpoint idx, check value
    # If match, return
    # Else check which half to search, find new mid

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                # search right
                left = mid + 1
            else:
                right = mid - 1

        # not found
        return -1
