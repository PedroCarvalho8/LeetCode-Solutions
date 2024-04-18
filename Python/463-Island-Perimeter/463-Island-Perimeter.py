class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                parameter = []
                if grid[i][j] == 1: 
                    perimeter += 4
                
                    if i != len(grid)-1: parameter.append(grid[i+1][j]) 
                    if i != 0: parameter.append(grid[i-1][j])
                    if j != len(grid[0])-1: parameter.append(grid[i][j+1])
                    if j != 0: parameter.append(grid[i][j-1])

                for k in parameter:
                    if (k == 1):
                        perimeter -= 1
        
        return perimeter
        
