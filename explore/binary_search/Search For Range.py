# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/

# Went off-rails a bit... quite hacky / overly complex
# Refactor start/end search to a function

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        left, right = 0, len(nums) - 1
         
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                start, end = mid, mid
                # now mid in the range
                #print(f"Found mid in the range: {mid}")
                
                # Search range start
                subleft, subright = left, mid - 1
                while subleft <= subright:
                    submid = (subleft + subright) // 2
                    if nums[submid] < target:
                        subleft = submid + 1
                    else:
                        start = submid
                        #print(f"New range start {start}")
                        subright = submid - 1
                    if subleft > subright:
                        break
                
                # Search range end
                subleft, subright = mid + 1, right
                while subleft <= subright:
                    submid = (subleft + subright) // 2
                    if nums[submid] > target:
                        subright = submid - 1
                    else:
                        end = submid
                        #print(f"New range end {end}")
                        subleft = submid + 1
                    if subleft > subright:
                        break  
                        
                break

        return [start, end]
