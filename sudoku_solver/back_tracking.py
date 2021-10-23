class BackTracking:
    backtracks = 0

    @staticmethod
    def is_in_row(sudoku: list, val: int, row: int) -> bool:
        return val in sudoku[row]

    @staticmethod
    def is_in_column(sudoku: list, val: int, col: int) -> bool:
        column = []
        for line in sudoku:
            column.append(line[col])
        return val in column

    @staticmethod
    def get_grid(sudoku: list, row: int, col: int) -> list:
        grid_line = row // 3
        grid_col = col // 3

        grid = []
        for line_num in range(grid_line * 3, grid_line * 3 + 3):
            line = sudoku[line_num]
            grid.append(line[grid_col * 3:grid_col * 3 + 3])

        return grid

    @staticmethod
    def is_in_grid(sudoku: list, val: int, row: int, col: int) -> bool:
        grid = BackTracking.get_grid(sudoku, row, col)
        for line in grid:
            if val in line:
                return True
        return False

    @staticmethod
    def is_complete(sudoku: list, ) -> bool:
        for line in sudoku:
            if 0 in line:
                return False
        return True

    @staticmethod
    def print_solution(sudoku: list, ):
        for line in sudoku:
            print(line)

    def solve(self, sudoku):
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if sudoku[row][col] == 0:
                for val in range(1, 10):
                    if not self.is_in_row(sudoku, val, row):
                        if not self.is_in_column(sudoku, val, col):
                            if not self.is_in_grid(sudoku, val, row, col):
                                sudoku[row][col] = val
                                if self.solve(sudoku):
                                    return True
                                else:
                                    sudoku[row][col] = 0
                self.backtracks = self.backtracks + 1
                print(f"Backtrack {self.backtracks}")
                return False
        if self.is_complete(sudoku):
            self.print_solution(sudoku)
            return True
        else:
            return False
