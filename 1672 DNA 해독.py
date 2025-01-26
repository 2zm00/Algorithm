decoding_table = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
}

def decode_dna_optimized(sequence):
    stack = list(sequence)  # 문자열을 스택으로 변환
    while len(stack) > 1:
        last = stack.pop()
        second_last = stack.pop()
        decoded = decoding_table[second_last][last]
        stack.append(decoded)
    return stack[0]

# 입력 받기
n = int(input())
sequence = input()
print(decode_dna_optimized(sequence))
