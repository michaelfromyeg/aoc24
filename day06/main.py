# Auto-generated by Puzzles

import copy
from enum import Enum

UP = [-1, 0]
DN = [1, 0]
LT = [0, -1]
RT = [0, 1]

PERSON = "^"
STARTING_DIRECTION: tuple[int, int] = UP


def turn(direction: tuple[int, int]) -> tuple[int, int]:
    match direction:
        case [-1, 0]:
            return RT
        case [0, 1]:
            return DN
        case [1, 0]:
            return LT
        case [0, -1]:
            return UP


def move(position: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    return (position[0] + direction[0], position[1] + direction[1])


class Cell(Enum):
    FREE = "."
    OBSTRUCTION = "#"


def part_one():
    """
    Solution to the puzzle.
    """
    with open("day06/input.txt") as f:
        lines = f.readlines()

        grid: list[list[Cell]] = []
        for i, line in enumerate(lines):
            if line.strip() == "":
                continue

            row: list[Cell] = []
            for j, c in enumerate(line.strip()):
                if c == PERSON:
                    starting_position = (i, j)
                    row.append(Cell.FREE)
                elif c == Cell.FREE.value:
                    row.append(Cell.FREE)
                else:
                    row.append(Cell.OBSTRUCTION)
            grid.append(row)

        # Debugging!
        # for i, row in enumerate(grid):
        #     for j, c in enumerate(row):
        #         if (i, j) == starting_position:
        #             print(PERSON, end="")
        #         else:
        #             print(c.value, end="")
        #     print()

        # rows, columns
        m, n = len(grid), len(grid[0])

        visited: set[tuple[int, int]] = set()

        tort, tort_dir = starting_position, STARTING_DIRECTION
        hare, hare_dir = starting_position, STARTING_DIRECTION
        visited.add(hare)

        # there's a weird edge case at the start, just hack around it
        hare = move(hare, hare_dir)
        visited.add(hare)

        hare = move(hare, hare_dir)
        visited.add(hare)

        tort = move(tort, tort_dir)

        while tort != hare:
            # move the hare, move the tort
            for _ in range(2):
                maybe_hare = move(hare, hare_dir)
                if (
                    maybe_hare[0] < 0
                    or maybe_hare[1] < 0
                    or maybe_hare[0] >= m
                    or maybe_hare[1] >= n
                ):
                    print(len(visited))
                    return

                maybe_obj = grid[maybe_hare[0]][maybe_hare[1]]

                while maybe_obj == Cell.OBSTRUCTION:
                    hare_dir = turn(hare_dir)
                    maybe_hare = move(hare, hare_dir)
                    maybe_obj = grid[maybe_hare[0]][maybe_hare[1]]

                hare = maybe_hare
                visited.add(hare)

            for _ in range(1):
                maybe_tort = move(tort, tort_dir)
                maybe_obj = grid[maybe_tort[0]][maybe_tort[1]]

                while maybe_obj == Cell.OBSTRUCTION:
                    tort_dir = turn(tort_dir)

                    maybe_tort = move(tort, tort_dir)
                    maybe_obj = grid[maybe_tort[0]][maybe_tort[1]]

                tort = maybe_tort

        # loop coverage
        print(len(visited))


def traverse(grid, m, n, starting_position):
    visited: set[tuple[int, int]] = set()

    tort, tort_dir = starting_position, STARTING_DIRECTION
    hare, hare_dir = starting_position, STARTING_DIRECTION
    visited.add(hare)

    while True:
        for _ in range(1):
            maybe_tort = move(tort, tort_dir)
            if (
                maybe_tort[0] < 0
                or maybe_tort[1] < 0
                or maybe_tort[0] >= m
                or maybe_tort[1] >= n
            ):
                # print(len(visited))
                return 0

            maybe_obj = grid[maybe_tort[0]][maybe_tort[1]]
            while maybe_obj == Cell.OBSTRUCTION:
                tort_dir = turn(tort_dir)

                maybe_tort = move(tort, tort_dir)
                maybe_obj = grid[maybe_tort[0]][maybe_tort[1]]

            tort = maybe_tort
            # print("tort visiting", tort)

        for _ in range(2):
            maybe_hare = move(hare, hare_dir)
            if (
                maybe_hare[0] < 0
                or maybe_hare[1] < 0
                or maybe_hare[0] >= m
                or maybe_hare[1] >= n
            ):
                # print(len(visited))
                return 0

            maybe_obj = grid[maybe_hare[0]][maybe_hare[1]]

            while maybe_obj == Cell.OBSTRUCTION:
                hare_dir = turn(hare_dir)
                maybe_hare = move(hare, hare_dir)
                maybe_obj = grid[maybe_hare[0]][maybe_hare[1]]

            hare = maybe_hare
            visited.add(hare)
            # print("hare visitng", hare)

        if tort == hare and tort_dir == hare_dir:
            break
    return 1


def part_two():
    """
    Solution to the puzzle.
    """
    with open("day06/input.txt") as f:
        lines = f.readlines()

        grid: list[list[Cell]] = []
        for i, line in enumerate(lines):
            if line.strip() == "":
                continue

            row: list[Cell] = []
            for j, c in enumerate(line.strip()):
                if c == PERSON:
                    starting_position = (i, j)
                    row.append(Cell.FREE)
                elif c == Cell.FREE.value:
                    row.append(Cell.FREE)
                else:
                    row.append(Cell.OBSTRUCTION)
            grid.append(row)

        # Debugging!
        # print("===")
        # for i, row in enumerate(grid):
        #     for j, c in enumerate(row):
        #         if (i, j) == starting_position:
        #             print(PERSON, end="")
        #         else:
        #             print(c.value, end="")
        #     print()
        # print("===")

        # rows, columns
        m, n = len(grid), len(grid[0])

        # expected = []
        # (6,3)
        # (7,6)
        # (7,7)
        # (8,5)
        # (8,3)
        # (9,7)

        # bad (2,8) and (8,5)

        count = 0
        for idx in range(m):
            for jdx in range(n):
                # print("looking at", idx, jdx)
                if (idx, jdx) == starting_position:
                    continue
                if grid[idx][jdx] == Cell.OBSTRUCTION:
                    continue

                new_grid = copy.deepcopy(grid)
                new_grid[idx][jdx] = Cell.OBSTRUCTION

                val = traverse(new_grid, m, n, starting_position)
                count += val

                if val == 1:
                    # print("blah")
                    print("place one at ", idx, jdx, count)

                    # for testi, row in enumerate(new_grid):
                    #     for testj, c in enumerate(row):
                    #         if (testi, testj) == starting_position:
                    #             print(PERSON, end="")
                    #         else:
                    #             print(c.value, end="")
                    #     print()

                    # return 0

        print(count)


def test_solve():
    """
    Test cases for the solution.
    """
    # TODO: Add test cases
    assert True, "Add your test cases here"


if __name__ == "__main__":
    test_solve()
    part_one()
    part_two()