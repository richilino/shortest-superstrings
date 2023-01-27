from functools import reduce, lru_cache

@lru_cache(maxsize=None)
def ov(s: str, t: str) -> int:
	if s == t:
		return max(i for i in range(len(t)) if s.endswith(t[:i]))
	
	return max(i for i in range(len(t)+1) if s.endswith(t[:i]))

def merge(s: str, t: str) -> str:
	return f"{s}{t[ov(s,t):]}"

def concat(S: set) -> str:
	return reduce(lambda s, aggregate: merge(s, aggregate), S)