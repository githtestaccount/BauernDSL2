#!/usr/bin/env python3
# The source file is the 1st argument to the script

import sys
import importlib

# The source file is the 1st argument to the script
if len(sys.argv) != 2:
    print('usage: %s <src.bdsl>' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        mod = importlib.import_module(parts[0])
        getattr(mod, parts[3])(parts[2], parts[1], parts[4])

