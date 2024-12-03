"""
The smallest difference.
"""

if __name__ == "__main__":
    with open("day1/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        ls: list[int] = []
        rs: list[int] = []
        for line in lines:
            l, r = line.strip().split(" ")
            ls.append(int(l))
            rs.append(int(r))

        ls.sort()
        rs.sort()

        total = 0
        for l, r in zip(ls, rs):
            total += abs(l - r)
        print(total)
