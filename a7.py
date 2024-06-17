fname = input('Enter file name: ')
fhand = open(fname)
counter = 0
result = 0
for line in fhand:
    # if not line.startswith('X-DSPAM-Confidence:'):
    #     continue
    # pos = line.find(':')
    # fnum = float(line[pos + 1:].strip())
    # counter += 1 
    # result += fnum
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        fnum = float(line[pos + 1:].strip())
        counter += 1 
        result += fnum
result = result / counter
print('Average spam confidence:', result)