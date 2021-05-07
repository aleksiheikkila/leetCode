class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
            
        i = 0
        for num, count in enumerate(counts):
            for idx in range(i, i + count):
                nums[idx] = num
            i += count

    def sortColors_dutch_flag_prob(self, nums):
        # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1