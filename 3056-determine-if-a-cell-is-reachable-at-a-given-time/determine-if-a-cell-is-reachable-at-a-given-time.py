class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        # Calculate the absolute differences in x and y coordinates between the start and target points.
        xDistance = abs(sx - fx)
        yDistance = abs(sy - fy)
        
        # Calculate the minimum Manhattan distance (minimum steps) to reach the target.
        min_dist = min(xDistance, yDistance) + abs(yDistance - xDistance)

        if min_dist == 0:
            if t == 1:
                return False  
            else:
                return True 
        return t >= min_dist  
