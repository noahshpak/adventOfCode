from functools import reduce
from typing import List, Tuple

import fire


class RepeatingTopology:
    def __init__(self, topology: List[List[bool]]):
        self._topology = topology
        self.num_rows = len(topology)
        self.num_cols = len(topology[0])

    def __getitem__(self, row_col: Tuple[int, int]):
        row, col = row_col
        return self._topology[row % self.num_rows][col % self.num_cols]


def _is_tree(s: str) -> bool:
    return s == "#"


def read_input(filename: str) -> RepeatingTopology:
    with open(filename, "r") as f:
        return RepeatingTopology(topology=[[_is_tree(s) for s in line.strip()] for line in f.readlines()])


def count_num_trees(topology_file: str, right=3, down=1) -> int:
    topology: RepeatingTopology = read_input(topology_file)
    trees = 0
    row, col = 0, 0
    while row < topology.num_rows - down:
        row, col = row + down, col + right
        if topology[row, col]:
            trees += 1
    return trees


def part2(topology_file: str, slopes=((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))) -> int:
    return reduce(lambda x, y: x * y, (count_num_trees(topology_file, right=right, down=down) for right, down in slopes), 1)


if __name__ == "__main__":
    fire.Fire()
