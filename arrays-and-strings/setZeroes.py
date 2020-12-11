class Solution(object):
    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("============================")

    def set_col_to_0(self, matrix, idx):
        for row in matrix:
            row[idx] = 0
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Determine what should become a 0 row or col
        for ridx, row in enumerate(matrix):
            for cidx, item in enumerate(row):
                if item == 0:
                    # edge case 1: 1st row 1st col needs to go
                    if ridx == 0 and cidx == 0:
                        matrix[0][0] = "z"
                    # edge case 2: some col in the first row needs to go
                    # which means the entire first row needs to go too, but
                    # not the first col
                    elif ridx == 0:
                        # if we alr determined that the entire first row and
                        # col need to go, then dont really need to do anything
                        # mark that this row needs to go too.
                        # however, if we are not killing off the first row + col,
                        # then we say that only this row needs to go
                        if matrix[0][0] == "z":
                            matrix[0][cidx] = "y"
                        else:
                            matrix[0][cidx] = "y"
                            matrix[0][0] = "x"
                    # we are not dealing with the first row, but the first col is
                    # still an edge case. if we are in the first col, and 0,0 is z,
                    # then dont do anything, just mark the row to be deleted
                    # however, if we are in the first col, and 0,0 is marked as x,
                    # we change it to z
                    else:
                        if cidx == 0:
                            if matrix[0][0] == "z":
                                row[0] = "x"
                            elif matrix[0][0] == "x":
                                matrix[0][0] = "z"
                                row[0] = "x"
                            else:
                                matrix[0][0] = "y"
                                row[0] = "x"

                        else:
                            row[0] = "x"
                            matrix[0][cidx] = "y"
        
        self.print_matrix(matrix)
        # start at 2nd row, 1st row contains impt info
        for i in range(1, len(matrix)):
            if matrix[i][0] == "x":
                matrix[i] = [0] * len(row)
        
        # fix all the columns starting at 2nd col
        for idx in range(len(matrix[0])):
            if matrix[0][idx] == "y":
                self.set_col_to_0(matrix, idx)
        
        # fix first row and col if need be
        if matrix[0][0] == "z":
            matrix[0] = [0] * len(matrix[0])
            self.set_col_to_0(matrix, 0)
        elif matrix[0][0] == "x":
            matrix[0] = [0] * len(matrix[0])
        elif matrix[0][0] == "y":
            self.set_col_to_0(matrix, 0)


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# Solution().print_matrix(matrix)
# Solution().setZeroes(matrix)
# Solution().print_matrix(matrix)

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Solution().print_matrix(matrix)
# Solution().setZeroes(matrix)
# Solution().print_matrix(matrix)


# matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
# Solution().print_matrix(matrix)
# Solution().setZeroes(matrix)
# Solution().print_matrix(matrix)

matrix = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]        
Solution().print_matrix(matrix)
Solution().setZeroes(matrix)
Solution().print_matrix(matrix)