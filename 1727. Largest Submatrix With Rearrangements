class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        colConsecOnes = [[0]*n for _ in range(m)]
        
        # For each column, find the number of consecutive ones ending at each position.
        for j in range(n):
            count = 0
            for i in range(m):
                if matrix[i][j] == 1:
                    count += 1
                else:
                    count = 0
                colConsecOnes[i][j] = count
        
        # For each row, rearrange columns optimally by sorting heights
        largestArea = 0
        for i in range(m):
            colConsecOnes[i].sort()  # ascending
            for j in range(n):
                height = colConsecOnes[i][j]
                width = n - j
                largestArea = max(largestArea, height * width)

        return largestArea
        
