"""
ID: your_id_here
LANG: PYTHON3
TASK: ride
"""

f = open('ride.in', 'r')
g = open('ride.out', 'w')
readfile = f.readlines()
commetname = readfile[0]
groupname = readfile[1]
commetname = commetname.lower()
groupname = groupname.lower()
commetname = list(commetname)
groupname = list(groupname)
commetnamenum = []
groupnamenum = []
for character in commetname:
    number = ord(character) - 96
    commetnamenum.append(number)
for character in groupname:
    numbe = ord(character) - 96
    groupnamenum.append(numbe)
del commetnamenum [-1]
del groupnamenum [-1]
mc = 1
gc = 1
for x in range(len(commetnamenum)):
    mc = mc * commetnamenum[x]
for x in range(len(groupnamenum)):
    gc = gc * groupnamenum[x]

gc = gc % 47
mc = mc % 47
if gc == mc:
    g.write ("GO" + '\n')
    g.close()
else:
    g.write ("STAY" + '\n')
    g.close()
