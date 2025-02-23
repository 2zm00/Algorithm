import sys

# Use sys.stdin for fast input reading
input = sys.stdin.readline

# Read number of items N and maximum weight K
N, K = map(int, input().split())

# Initialize the DP array with zeros for each possible weight [0, K]
dp = [0] * (K + 1)

# Process each item
for _ in range(N):
    weight, value = map(int, input().split())
    # Update dp array in reverse to prevent item reuse
    for cur_weight in range(K, weight - 1, -1):
        dp[cur_weight] = max(dp[cur_weight], dp[cur_weight - weight] + value)

# Output the maximum value that can be achieved with weight exactly up to K
print(dp[K])
