"""
The smallest difference.
"""

if __name__ == "__main__":
    with open("day1/input2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        ls: list[int] = []
        rs: list[int] = []
        for line in lines:
            if not line.strip():
                continue

            l, r = line.strip().split("   ")
            ls.append(int(l))
            rs.append(int(r))

        ls.sort()
        rs.sort()

        total = 0
        for l, r in zip(ls, rs):
            total += abs(l - r)
        print(total)

        total2 = 0

        r_map = {}
        for r in rs:
            if r in r_map:
                r_map[r] += 1
            else:
                r_map[r] = 1

        for l in ls:
            if l not in r_map:
                continue
            total2 += l * r_map[l]

        print(total2)
