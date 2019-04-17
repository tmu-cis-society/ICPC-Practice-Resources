n = int(input('n: '))

num_comparisons = int((n * (n))/4)

print(num_comparisons)

sum_comparisons = 0
current_num = 1

while True:
	sum_comparisons += n
	n = n - 1
	if sum_comparisons >= num_comparisons:
		print(current_num)
		break

	current_num = current_num + 1
