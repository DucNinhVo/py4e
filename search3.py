fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be open: ',fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count += 1
print('There are ', count, 'subject lines in ', fname) 