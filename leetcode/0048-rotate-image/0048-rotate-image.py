class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        # transpose the matrix (swap across diagonal)
        for i in range(n):
            for j in range(i, n):
                # swap matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse each row
        for i in range(n):
            # reverse the row in-place
            matrix[i].reverse()