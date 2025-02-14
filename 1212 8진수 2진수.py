octal = input().strip()
if octal == '0':
    print(0)
else:
    binary = []
    for i, digit in enumerate(octal):
        bin_str = bin(int(digit))[2:]
        if i == 0:
            binary.append(bin_str)
        else:
            binary.append(bin_str.zfill(3))
    print(''.join(binary))
