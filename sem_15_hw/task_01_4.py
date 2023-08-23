"""Eight queen chess puzzle
"""
import argparse
import random
from typing import Callable
import logging

BOARD_SIZE = 8
QUEENS_QTY = 8

logging.basicConfig(filename='queens_coords.log', filemode='w', level=logging.INFO, encoding='utf-8',
                    format='{msg}', style='{')
logger = logging.getLogger(__name__)


def log_coords(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info('\n'.join(pretty_board(board) for board in result))
        return result

    return wrapper


def check_queens(coords: list[tuple[int, int]]) -> bool:
    """Check queens coordinates for partially random generator.
    Skips checking queens in one row and col
    """
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            if coords[i][0] + coords[i][1] == coords[j][0] + coords[j][1]:
                return False
            if coords[i][0] - coords[i][1] == coords[j][0] - coords[j][1]:
                return False

    return True


def generate_coords(queens_qty: int) -> list[tuple[int, int]]:
    """Partially random queens coordinates generator.
    Generates queens only in unique rows and cols.
    """
    queens_coords = []
    rows = [row for row in range(1, BOARD_SIZE + 1)]
    cols = [col for col in range(1, BOARD_SIZE + 1)]
    for _ in range(queens_qty):
        row = random.choice(rows)
        rows.remove(row)
        col = random.choice(cols)
        cols.remove(col)
        queens_coords.append((row, col))
    return queens_coords


@log_coords
def find_success_coords(queens_qty: int, coords_qty: int = 1) -> list[set[tuple[int, int]]]:
    """Find list of unique queen coordinates using generator function in param.
    Works faster with partially random coordinates generation.
    """
    safe_coords = []
    while len(safe_coords) < coords_qty:
        coords = generate_coords(queens_qty)
        if check_queens(coords) and set(coords) not in safe_coords:
            safe_coords.append(set(coords))
    return safe_coords


def pretty_board(coords: set[tuple[int, int]]):
    """Returns emoji pretty checkmate board with queens on it
    """
    board = [['⬜️' if (i + j) % 2 == 0 else '⬛️' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    for coord in coords:
        board[coord[0] - 1][coord[1] - 1] = '👑'

    return str(coords) + '\n' + '\n'.join(str(' '.join(row)) for row in board) + '\n'


def parse():
    parser = argparse.ArgumentParser(prog='Queens coordinates',
                                     description='Finds defined quantity of queens safe coordinates',
                                     epilog='Queens quantity and Coordinates quantity can be chose')
    parser.add_argument('-q', '--queens', default=QUEENS_QTY, help='Date to check', type=int)
    parser.add_argument('-c', '--coordinates', default=1, help='Date to check', type=int)
    args = parser.parse_args()
    return find_success_coords(args.queens, args.coordinates)


if __name__ == '__main__':
    parse()
