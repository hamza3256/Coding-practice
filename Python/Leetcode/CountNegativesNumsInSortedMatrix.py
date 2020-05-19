class Solution(object):
    def countNegatives(self, grid):
        c = 0
        for j in grid:
            for i in range(len(j)):
                if j[i] < 0:
                    c +=1       
        return c