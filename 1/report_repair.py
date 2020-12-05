"""https://adventofcode.com/2020/day/1"""
from collections import Counter
from functools import reduce
from typing import List, Tuple

import fire


class ReportRepair:
    def __init__(self):
        self._result = None

    def _read_input(self, filename: str) -> List[int]:
        with open(filename, 'r') as f:
            return map(int, f.readlines())

    def twosum(self, file_of_ints: str, goal: int) -> Tuple[int, int]:
        ints = self._read_input(file_of_ints)
        search_space = Counter(ints)
        for i in search_space:
            int_needed = goal - i
            if int_needed in search_space:
                if int_needed == i and search_space[i] < 2:
                    continue
                self._result = i, goal - i
                return self
        
    def threesum(self, file_of_ints: str, goal: int) -> Tuple[int, int, int]:
        ints = self._read_input(file_of_ints)
        search_space = sorted(ints)
        for idx in range(len(search_space)):
            left = idx + 1
            right = len(search_space) - 1
            while left < right:
                current_sum = search_space[idx] + search_space[left] + search_space[right]
                if current_sum == goal:
                    self._result = search_space[idx], search_space[left], search_space[right]
                    return self
                elif current_sum < goal:
                    left += 1
                elif current_sum > goal:
                    right -= 1
    
    def product(self): 
        if self._result is None:
            return "No Result Found"
        return reduce(lambda x, y: x * y, self._result, 1)

if __name__ == '__main__':
    fire.Fire(ReportRepair)