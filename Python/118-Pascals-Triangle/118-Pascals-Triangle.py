class Solution(object):
    def generate(self, numRows):
        for i in range (numRows):
            list = [1] * numRows
            for j in range (i+1):
                list[j] = [1] * (j+1)

        for i in range (numRows):
            for j in range (i):
                if not(j == 0 or j == numRows-1):
                    list[i][j] = list[i-1][j] + list[i-1][j-1]
        
        return list
