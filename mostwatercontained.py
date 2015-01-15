class Solution:
    # @return an integer
    def maxArea(self, height):
        last=len(height)-1
        start=0
        area=0
        while start < last:
            area = max(area, (last-start)*min(height[start],height[last]))
            if height[last] > height[start]:
                start+=1
            else:
                last-=1
        return area