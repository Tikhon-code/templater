import sys
import lib

argv = sys.argv[1:]
argc = len(argv)

files = []

pos = 0

while pos < argc:
    t = argv[pos]
    pos += 1
    
    files.append(t)

for file in files:
    lib.lscript.lscript.run(file)
