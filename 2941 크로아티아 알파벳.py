croatian = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()

for pattern in croatian:
    word = word.replace(pattern, '*')

print(len(word))
