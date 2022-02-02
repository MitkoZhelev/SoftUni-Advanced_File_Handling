import re
file = open("text.txt")

count = 0

for count,line in enumerate(file.readlines()):
    if count % 2 != 0:
        continue
    line = re.sub('[-,.!?]','@',line)
    line = ' '.join(reversed(line.split()))
    print(line)

file.close()