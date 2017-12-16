## https://www.codechef.com/problems/CNOTE
# 3
# 3 1 2 2
# 3 4
# 2 2    
# 3 1 2 2
# 2 3
# 2 3    
# 3 1 2 2
# 1 1
# 1 2

def main():
	test_cases = int(input())

	while(test_cases > 0):
		test_cases =  test_cases - 1 

		poetry_length, pages_left, number_of_notebooks, money = [int(b) for b in input().split()]
		pages_needed = poetry_length - pages_left

		flag = False
		for book_index in range(number_of_notebooks):
			pages, cost = [int(b) for b in input().split()] 
			if pages >= pages_needed and cost <= money:
				flag = True
				break;

		if flag:
			print("LuckyChef")
		else:
			print("UnluckyChef")


main()