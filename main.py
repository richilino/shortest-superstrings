import time
from greedy import greedy
from mgreedy import mgreedy
from tgreedy import tgreedy

def read_seq(path = "reads1.txt") -> set[str]:
    with open(path, 'r') as file:
        return set([str(line.strip()) for line in file.readlines()])

def process_greedy(path = None) -> None:
    s = read_seq(path)
    start = time.perf_counter()
    res = list(greedy(s))[0]
    end = time.perf_counter()
    print(f"Greedy found {res} ({len(res)})")
    print(f"Elapsed time: {end-start}")

def process_mgreedy(path = None) -> None:
    s = read_seq(path)
    start = time.perf_counter()
    res = mgreedy(s)
    end = time.perf_counter()
    print(f"MGreedy found {res} ({len(res)})")
    print(f"Elapsed time: {end-start}")

def process_tgreedy(path = None) -> None:
    s = read_seq(path)
    start = time.perf_counter()
    res = list(tgreedy(s))[0]
    end = time.perf_counter()
    print(f"TGreedy found {res} ({len(res)})")
    print(f"Elapsed time: {end-start}")


"""
s = {"ate", "half", "lethal", "alpha", "alfalfa"}
s2 = read_seq()
res = list(greedy(s2))[0]
print(f"Greedy found {res} ({len(res)})")

s = {"ate", "half", "lethal", "alpha", "alfalfa"}
s2 = read_seq()
res = mgreedy(s2)
print(f"MGreedy found {res} ({len(res)})")

s = {"ate", "half", "lethal", "alpha", "alfalfa"}
s2 = read_seq()
res = list(tgreedy(s2))[0]
print(f"TGreedy found {res} ({len(res)})")
"""