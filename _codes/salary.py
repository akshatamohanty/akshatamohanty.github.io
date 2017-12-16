## https://www.codechef.com/problems/SALARY
# Input:
# 2
# 3
# 1 2 3
# 2
# 42 42

# Output:
# 3
# 0

def operation(unlucky_worker, worker_salaries):
	new_salaries = []
	for worker in range(len(worker_salaries)):
		if worker == unlucky_worker:
			new_salaries.append(worker_salaries[worker])
		else:
			new_salaries.append(worker_salaries[worker] + 1)
	return new_salaries

def isEqual(worker_salaries):
	return len(set(worker_salaries)) <= 1

def main():
	test_cases = int(input())

	while(test_cases > 0):
		test_cases =  test_cases - 1 

		number_of_workers = int(input())
		worker_salaries = [ int(salary) for salary in input().split() ]

		count = 0
		while(isEqual(worker_salaries) == False):
			unlucky_worker= worker_salaries.index(max(worker_salaries))
			worker_salaries = operation(unlucky_worker, worker_salaries)
			count = count + 1
		print(count)

main()