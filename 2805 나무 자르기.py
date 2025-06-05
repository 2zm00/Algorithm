
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

start =0
end = max(nums)
result =0

while start <= end:
	mid = (start + end) // 2
	total = 0
	for num in nums:
		if num > mid:
			total += num - mid
	
	if total >= m:
		result = mid
		start = mid +1
	else:
		end = mid - 1

print(result)


# 문제풀이
# 
