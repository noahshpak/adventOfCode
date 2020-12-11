import fire
from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [l.strip() for l in f.readlines()]


def seat_coords(binary_partition: str) -> int:
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    for char in binary_partition:
        if char == "F":
            row_min, row_max = row_min, ((row_min + row_max) // 2)
        elif char == "B":
            row_min, row_max = ((row_min + row_max) // 2) + 1, row_max
        elif char == "R":
            col_min, col_max = ((col_min + col_max) // 2) + 1, col_max
        elif char == "L":
            col_min, col_max = col_min, ((col_min + col_max) // 2)
    return row_max, col_max


def seat_id(seat_coords: Tuple[int, int]):
    row, col = seat_coords
    return row * 8 + col


def sanity_check(filename):
    return max(seat_id(seat_coords(binary_partition)) for binary_partition in read_input(filename))


def find_me(filename):
    coords = [seat_coords(binary_partition) for binary_partition in read_input(filename)]
    seat_ids = {seat_id(coords) for coords in coords}
    for r in range(127):
        for c in range(8):
            if r == 0 or r == 127:
                continue
            sid = seat_id((r, c))
            if sid not in seat_ids and sid + 1 in seat_ids and sid - 1 in seat_ids:
                return sid


if __name__ == "__main__":
    fire.Fire()