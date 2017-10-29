## https://www.codechef.com/problems/FRGTNLNG

# 2
# 3 2
# piygu ezyfo rzotm
# 1 piygu
# 6 tefwz tefwz piygu ezyfo tefwz piygu
# 4 1
# kssdy tjzhy ljzym kegqz
# 4 kegqz kegqz kegqz vxvyj

# Output:
# YES YES NO 
# NO NO NO YES


def main():

	test_cases = int(input())

	while(test_cases > 0):
		test_cases = test_cases - 1

		dictionary_size, phrases_count = [int(b) for b in input().split()]
		dictionary = input().split()

		all_words = {}
		for phrase in range(phrases_count):
			phrase_input = input().split()
			phrase_input.pop()
			for word in phrase_input:
				if word in all_words:
					all_words[word] = all_words[word] + 1
				else:
					all_words[word] = 1


		for word in dictionary:
			if word in all_words:
				print("YES", end=" ")
			else:
				print("NO", end=" ")

		print();

main()
