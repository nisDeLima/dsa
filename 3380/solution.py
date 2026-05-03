class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        seen = set()
        res = -1
        
        for x, y in points:
            for x2, y2 in seen:
                # Check if we have a valid rectangle
                if (x, y2) in seen and (x2, y) in seen:
                    # Calculate bounds once, like a smart person
                    min_x, max_x = (x, x2) if x < x2 else (x2, x)
                    min_y, max_y = (y, y2) if y < y2 else (y2, y)
                    
                    # Validate: no stray points inside
                    valid = True
                    for px, py in points:
                        if min_x <= px <= max_x and min_y <= py <= max_y:
                            if (px, py) not in {(x, y), (x2, y2), (x, y2), (x2, y)}:
                                valid = False
                                break
                    
                    if valid:
                        res = max(res, (max_x - min_x) * (max_y - min_y))
            
            seen.add((x, y))
        
        return res
