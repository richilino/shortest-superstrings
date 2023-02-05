from functools import reduce
from itertools import product
from base import ov, merge, concat

def choose(S: set) -> tuple[str,str]:
	return reduce(lambda st, xy: (st[0],st[1]) 
								if ov(st[0],st[1]) > ov(xy[0],xy[1])
								else (xy[0],xy[1]), product(S, repeat=2))

def mgreedy(S: set) -> str:
	T = set()

	while S:
		(s,t) = choose(S)

		if (s == t):
			S.remove(s)
			T.add(s)
		else:
			S.difference_update({s,t})
			S.add(merge(s,t))

	return concat(T)