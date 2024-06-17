name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# loop through handel and add time to a list
time_list = []
for line in handle:
    words = line.split()
    if len(words) == 0: 
        continue
    if words[0] != 'From': 
        continue
    hour = words[5].split(':')[0]
    time_list.append(hour)

# loop through list, count time and add to a dict
time_dis = {}
for time in time_list:
    time_dis[time] = time_dis.get(time,0) + 1

# create a list of tuples from the dict and sort it
sorted_time_dis = sorted(list(time_dis.items()))

for time,count in sorted_time_dis:
    print(time,count)