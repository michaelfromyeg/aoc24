"""
Corrupted multiplication.

TODO(michaelfromyeg): regex? or at least isalpha instead
"""

if __name__ == "__main__":
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        string = f.readlines()[0].strip()
        candidates = string.split("mul")

        total = 0
        for candidate in candidates:
            try:
                li, ri = candidate.index("("), candidate.index(")")
                if li != 0:
                    continue
                candidate = candidate[1:ri]

                l, r = candidate.split(",")
                if l.strip() != l or r.strip() != r:
                    continue
                total += int(l) * int(r)
            except (
                ValueError
            ):  # catch-all for "substring not found" and "invalid literal for int()"
                continue

        print(total)
