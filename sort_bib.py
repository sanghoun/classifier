import sys

f1 = open(sys.argv[1])
lines = f1.readlines()
f1.close()

ref = {}

f1 = open(sys.argv[1], 'w')
f2 = open(sys.argv[1]+".bck", 'w')

buf = ""

for line in lines:  
    f2.write(line)
    buf += line

    if line[0] == '@':
        entry = line[line.find("{")+1:line.find(",")]
        if entry in ref.keys():
            print "duplicated entry: " + entry
            sys.exit()
    if line[0] == '}':
        ref[entry] = buf.strip()
        buf = ""

ks = ref.keys()
ks.sort()

for k in ks:
    f1.write(ref[k])
    f1.write("\n\n")

f1.close()
f2.close()
