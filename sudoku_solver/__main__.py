import io

from sudoku_solver.back_tracking import BackTracking

easy_str = """120070560
507932080
000001000
010240050
308000402
070085010
000700000
080423701
034010028
"""

hardest_str = """800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400
"""


def _input(string):
    buf = io.StringIO(string)
    for line in buf.readlines():
        yield line[:-1]


def get_sudoku(difficulty):
    sudoku_str = {'easy': easy_str,
                  'hard': hardest_str
                  }.get(difficulty)

    return [x for x in sudoku_str.split('\n') if len(x) > 1]


if __name__ == '__main__':
    sudoku = []
    for line in get_sudoku('easy'):
        sudoku.append([int(x) for x in line])

    original = sudoku.copy()
    BackTracking().solve(sudoku)
