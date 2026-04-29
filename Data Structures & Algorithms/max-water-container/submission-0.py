class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # A = l x w
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            dist = r - l
            height = min(heights[l], heights[r])
            curr_area = height * dist
            if curr_area > max_area:
                max_area = curr_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
            
