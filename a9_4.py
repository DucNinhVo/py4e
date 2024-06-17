name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# loop through the handle, add sender's email to a list
senders_list = list()
for line in handle:
    if 'From ' in line: 
        # should maybe use startwith because 'From ' can also be in the middle off the line
        # or words[0] == 'From '
        words = line.split()
        senders_list.append(words[1])

# loop through the list, count times each sender sent email, add key and value to a dict
senders_dict = dict() 
for sender in senders_list:
    senders_dict[sender] = senders_dict.get(sender,0) + 1

# looop through the dict.item(), find the one who send most email
max_count = None
max_sender = None
for sender,count in senders_dict.items():
    if max_count is None or count > max_count:
        max_count = count
        max_sender = sender

print(max_sender,max_count)