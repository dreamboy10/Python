앉힐 수 있는 최소 사람 수 = 2
앉힐 수 있는 최대 사람 수 = 10
전체 사람의 수 = 100
memo = {}

def 문제(남은 사람 수, 앉힌 사람 수):
	key = str([남은 사람 수, 앉힌 사람 수])

	if key in memo:
		return memo[key]
	if 남은 사람 수 < 0:
		return 0
	if 남은 사람 수 == 0:
		return 1

	count = 0
	for i in range(앉힌 사람 수, 앉힐 수 있는 최대 사람 수 + i):
		count += 문제(남은 사람 수 - i, i)

	memo[key] = count

	return count

print(문제(전체 사람의 수, 앉힐 수 있는 최소 사람 수))
