import os



_,_, files = next(os.walk('.'))

extention = {}

for file in files :

    ext = file.split('.')[-1]
    if ext not in extention:
        extention[ext] = []
    extention[ext].append(file)

with open(os.path.expanduser('~/Desktop/report.txt'),'w') as out_file:
    for ext in sorted(extention.keys()):
        files = sorted(extention[ext])
        out_file.write(f'.{ext}\n')
        for file in files :
            out_file.write(f'---{file}\n')
