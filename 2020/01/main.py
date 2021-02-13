import numpy as np
from itertools import combinations

"""
Before you leave, the Elves in accounting just need you to fix your expense
 report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
 multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
 them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""
"""
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers
 you a starfish coin they had left over from a past vacation.
 They offer you a second one if you can find three numbers in your expense
  report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366,
 and 675. Multiplying them together produces the answer, 241861950.
"""


def main():
    X = np.loadtxt("2020/01/input.txt", dtype=int)

    # For part 1, we can use vector intersection
    # Find the complement to 2020
    X_comp = 2020 - X
    # The entries that add up will be the intersection
    res = np.intersect1d(X, X_comp)
    print(f"Result of part 1: {np.prod(res)}")

    # For part 2, we will deal with the combinations
    for a, b, c in combinations(X, 3):
        if a + b + c == 2020:
            res = a * b * c
            break
    print(f"Result of part 2: {res}")


if __name__ == "__main__":
    main()
