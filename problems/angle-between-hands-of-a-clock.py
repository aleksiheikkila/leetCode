# https://leetcode.com/problems/angle-between-hands-of-a-clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Use 12 as the reference direction
        # clockwise from there -> angle increases
        
        minute_angle = minutes * 6  # 6 degrees per minute (60*6 = 360)
        hour_angle = ((hour % 12) + (minutes / 60)) * 30  # 30 degrees per hour
        
        angle_between = abs(minute_angle - hour_angle)
        
        # return the smallest angle: it's either angle or 360 - angle
        return min(angle_between, 360 - angle_between)
        
        
        