fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line: # if line.find('@uct.ac.za') == -1 
        continue    
    print(line)

