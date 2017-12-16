## https://www.codechef.com/problems/RAINBOWA

# Input
# 3
# 19
# 1 2 3 4 4 5 6 6 6 7 6 6 6 5 4 4 3 2 1
# 14
# 1 2 3 4 5 6 7 6 5 4 3 2 1 1
# 13
# 1 2 3 4 5 6 8 6 5 4 3 2 1

# Output
# yes
# no
# no

def main():
	test_cases = int(input())

	while(test_cases > 0):
		test_cases =  test_cases - 1 

		array_length = int(input())
		array = [ int(b) for b in input().split() ]

		flag = False
		index = 1
		# pass


main()