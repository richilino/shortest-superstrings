from functools import reduce
from itertools import product

def ov(s: str, t: str) -> int:
	if s == t:
		return max(i for i in range(len(t)) if s.endswith(t[:i]))
	
	return max(i for i in range(len(t)+1) if s.endswith(t[:i]))

def choose(S: set) -> tuple[str,str]:
	return reduce(lambda st, xy: (st[0],st[1]) if ov(st[0],st[1]) >= ov(xy[0],xy[1]) else (xy[0],xy[1]), product(S,repeat=2))

def merge(s: str, t: str) -> str:
	return f"{s}{t[ov(s,t):]}"

def concat(S: set) -> str:
	return reduce(lambda s, aggregate: s+aggregate if ov(s,aggregate) == 0 else merge(s, aggregate), S)

def mgreedy(S: set) -> str:
	T = set()

	while S:
		(s,t) = choose(S)

		if (s == t):
			S.remove(s)
			T.add(s)
		else:
			S.remove(s)
			S.remove(t)
			T.add(merge(s,t))

	return concat(T)


s = {"ate", "half", "lethal", "alpha", "alfalfa"}
res = mgreedy(s)
print(f"Greedy found {res} ({len(res)})")
