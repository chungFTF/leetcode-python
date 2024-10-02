# 59. Spiral Matrix II


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # Sol.1 Brute force
        # loop = n // 2
        # start_x = 0
        # count = 1
        # my_matrix = [[0] * n for _ in range(n)]

        # for i in range(1, loop + 1): # iteration
        #     # from left to right
        #     for idx in range(start_x, n - i):
        #         my_matrix[start_x][idx] = count
        #         count += 1

        #     # from up to bottom
        #     for idx in range(start_x, n - i):
        #         my_matrix[idx][n - i] = count
        #         count += 1

        #     # from right to left
        #     for idx in range(n - i, start_x, -1):
        #         my_matrix[n - i][idx] = count
        #         count += 1

        #     # from bottom to up
        #     for idx in range(n - i, start_x, -1):
        #         my_matrix[idx][start_x] = count
        #         count += 1
            
        #     start_x += 1
        
        # mid = n // 2
        # if(n % 2 == 1):
        #     my_matrix[mid][mid] = count

        # return my_matrix
        

        # Sol. 2 Recursive
        matrix = [[0] * n for _ in range(n)]
        fillMatrix(matrix, 0, n - 1, 0, n - 1, 1)
        return matrix

def fillMatrix(matrix: List[List[int]], top: int, bottom: int, left: int, right: int, num: int) -> None:
    if top > bottom or left > right:
        return
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    for i in range(top + 1, bottom + 1):
        matrix[i][right] = num
        num += 1
    # if top < bottom and left < right:
    for i in range(right - 1, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    for i in range(bottom - 1, top, -1):
        matrix[i][left] = num
        num += 1
    fillMatrix(matrix, top + 1, bottom - 1, left + 1, right - 1, num)

        