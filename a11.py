import re

# list comprehension, the [] should be removed
print(sum(int(num) for num in re.findall('[0-9]+',open('regex_sum_1907761.txt').read())))

handel = open('regex_sum_1907761.txt')
text = handel.read()
num_list = re.findall('[0-9]+',text)
sum = 0
for num in num_list:
    sum += int(num)
print(sum)

