import sys

for line in sys.stdin:
    content = line.rstrip('\n')
    while True:
        new_content = content.replace("BUG", "")
        if new_content == content:
            break
        content = new_content
    print(content)
