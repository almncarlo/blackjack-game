strategy = []

fh = open('1.txt','r')
for line in fh:
    strategy.append(line.lower())
fh.close()

fh = open('2.txt','w')
fh.writelines(strategy)
fh.close()