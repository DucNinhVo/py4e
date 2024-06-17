fhand = open('mbox-short.txt')

inp = fhand.read()
print(len(inp))
print(inp[:20])

count = 0
for line in fhand:
    count += 1
print(count)
