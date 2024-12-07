"""
Corrupted multiplication.
"""

import re

if __name__ == "__main__":
    with open("day3/input2.txt", "r", encoding="utf-8") as f:
        string = "".join(f.readlines()).strip()

        total = 0
        pattern = r"mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)"
        matches = re.findall(pattern, string)

        for match in matches:
            try:
                l, r = match
                total += int(l) * int(r)
            except ValueError as e:
                print(e)
                continue

        print(total)

        total2 = 0

        pattern1 = pattern
        mults = [(m.start(0), m.end(0)) for m in re.finditer(pattern1, string)]

        pattern2 = r"don't\(\)"
        donts = [m.end() for m in re.finditer(pattern2, string)]
        donts.sort()

        pattern3 = r"do\(\)"
        dos = [m.end() for m in re.finditer(pattern3, string)]
        dos.sort()

        for mult in mults:
            # I know there's a better way here, but this works!
            closest = max((x for x in dos + donts if x <= mult[0]), default=None)
            if closest in donts:
                continue
            l, r = string[mult[0] : mult[1]][4:-1].split(",")
            total2 += int(l) * int(r)

        print(total2)
