## https://www.codechef.com/problems/COPS
# Input:
# 3
# 4 7 8
# 12 52 56 8
# 2 10 2
# 21 75
# 2 5 8
# 10 51

# Output:
# 0
# 18
# 9


def main():
	test_cases = int(input())

	while(test_cases > 0):

		M, x, y = [ int(b) for b in input().split() ]
		pos = [int(p) for p in input().split()]
		pos.sort()

		limit = x*y; 
		safe = 0; 
		left_limit = 0
		right_limit = 0

		for police in pos:
			left = police - limit
			right = police + limit

			if left < 0:
				left = 0

			## if there is left overlap
			if left > right_limit:
				## compute houses between this limit and before
				safe = safe + (left - right_limit) - 1
				left_limit = left

			if right > right_limit:
				right_limit = right

		if (right_limit < 100):
			safe = safe + 100 - right_limit

		print(safe)

		test_cases =  test_cases - 1 

main()