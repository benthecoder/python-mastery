"""
1. read Data/portfolio.dat
2. sum of second column * third column

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44

how to store?

total_cost variable to increment += (2nd col * 3rd col)

to read file, use context manager `with`
"""

import os


def portfolio_cost(fname: str) -> int:
    if not os.path.isfile(fname):
        raise FileNotFoundError

    total_cost = 0.0
    with open(fname, "r") as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except ValueError as e:
                print(f"Couldn't parse: {repr(line)}")
                print(f"Reason: {e}")

    return total_cost


if __name__ == "__main__":
    print(portfolio_cost("../Data/portfolio.dat"))
    print(portfolio_cost("../Data/portfolio2.dat"))
    print(portfolio_cost("../Data/portfolio3.dat"))
