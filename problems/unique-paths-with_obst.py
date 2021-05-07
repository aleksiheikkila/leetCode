# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        num_rows, num_cols = len(obstacleGrid), len(obstacleGrid[0])
        
        unique_paths_to = [[0 if obstacleGrid[r][c] == 1 else 1 for c in range(num_cols)] 
                            for r in range(num_rows)]
        
        for row in range(num_rows):
            for col in range(num_cols):
                if row == 0 and col == 0 or obstacleGrid[row][col] == 1:
                    continue
                else:
                    # from up and left
                    unique_paths_to[row][col] = (unique_paths_to[row][col - 1] if col > 0 else 0) \
                                                + (unique_paths_to[row - 1][col] if row > 0 else 0)
                    
        return unique_paths_to[num_rows - 1][num_cols - 1]
                    