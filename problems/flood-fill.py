class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        img_rows, img_cols = len(image), len(image[0])
        
        if sr < 0 or sr >= img_rows or sc < 0 or sc >= img_cols:
            return image
        
        # infinite loop issue possible if newColor == color
        DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        color = image[sr][sc]
        if color == newColor:
            # in this case, we would just "replace" color with the same color. No need
            return image

        image[sr][sc] = newColor
        s = [(sr, sc)]
        #visited = set()
        
        while s:
            curr_r, curr_c = s.pop()
            #visited.add((curr_r, curr_c))
            
            for dr, dc in DELTAS:
                r = curr_r + dr
                c = curr_c + dc
                if r < 0 or c < 0 or r >= img_rows or c >= img_cols:
                    continue
                # else valid position
                if image[r][c] == color: # and (r, c) not in visited:
                    s.append((r, c))
                    image[r][c] = newColor
                    
        return image
                    

    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        
        if sr < 0 or sr >= R or sc < 0 or sc >= C:
            return image
        
        # Possible inf loop when newColor is == starting color
   
        color = image[sr][sc]
    
        def dfs(r, c):
            #if image[r][c] == color:
            image[r][c] = newColor

            if r >= 1:
                if image[r - 1][c] == color: dfs(r - 1, c)
            if r < R - 1:
                if image[r + 1][c] == color: dfs(r + 1, c)
            if c >= 1:
                if image[r][c-1] == color: dfs(r, c - 1)
            if c < C - 1:
                if image[r][c+1] == color: dfs(r, c + 1)

    
        dfs(sr, sc)
        return image
    
   