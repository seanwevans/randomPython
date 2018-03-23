def primes(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
	
def isprime(n):
	if n < 2: return(False)
	lim = int(n ** .5) + 1
	for i in range(2, lim):
		if n % i == 0:
			return(False)
	return(True)
	
if __name__ == "__main__":
	print("sean")