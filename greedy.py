from functools import reduce
from itertools import product
from base import ov, merge

def generate_product(S: set):
    return filter(lambda st: st[0] != st[1], product(S, repeat=2))

def choose(S: set) -> tuple[str,str]:
	return reduce(lambda st, xy: (st[0],st[1]) 
								if ov(st[0],st[1]) >= ov(xy[0],xy[1]) 
								else (xy[0],xy[1]), generate_product(S))

def greedy(S: set) -> str:
    
    while len(S) > 1:
        (s,t) = choose(S)
        S.difference_update({s,t})
        S.add(merge(s,t))

    return S
