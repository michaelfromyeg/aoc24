"""
Reports and levels.
"""


def is_safe(level: list[int]) -> bool:
    n = len(level)
    if n == 0 or n == 1:
        return True

    dir = 0
    prev = level[0]
    for i in range(1, n, 1):
        curr = level[i]
        diff = curr - prev
        if abs(diff) < 1 or abs(diff) > 3:  # the diff is too small or large
            return False
        elif dir == 0:  # dir is unset
            dir = diff // abs(diff)
        elif dir != diff / abs(diff):  # the dir doesn't match
            return False
        prev = curr  # continue!
    return True


def is_safe_after_dampening(level: list[int]) -> bool:
    n = len(level)
    for i in range(n):
        new_level = level[0:i] + level[(i + 1) : n]
        if is_safe(new_level):
            return True
    return False


if __name__ == "__main__":
    with open("day2/input2.txt", "r", encoding="utf-8") as f:
        reports = f.readlines()

        count = 0
        count2 = 0
        for report in reports:
            level = report.strip().split(" ")
            count += is_safe([int(x) for x in level])  # implicit bool to int
            count2 += is_safe_after_dampening([int(x) for x in level])
        print(count)
        print(count2)
