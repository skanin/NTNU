memo = {}


def test(prod):
	memo[0] = 1
	memo[1] = 1
	n = 2
	while True:
		for i in range(n, -1, -1):
			memo[n] = memo[n-1] + memo[n-2]

		if memo[n-1] * memo[n-2] == prod:
			return [memo[n-2], memo[n-1], True]
		elif memo[n-1] * memo[n-2] > prod:
			return [memo[n-2], memo[n-1], False]

		n += 1

print(test(4895))