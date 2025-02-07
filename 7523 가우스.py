import sys
input = sys.stdin.readline
t = int(input().strip())
for i in range(1, t + 1):
	n, m = map(int, input().split())
	# The number of terms in the sequence
	count = m - n + 1
	# Using the arithmetic series sum formula
	total_sum = count * (n + m) // 2
	
	# Print the scenario header and the result
	print("Scenario #{}:".format(i))
	print(total_sum)
	print()