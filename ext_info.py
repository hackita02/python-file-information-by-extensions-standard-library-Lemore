#!/user/bin/python3
from pathlib import Path
from collections import defaultdict
import sys

if len(sys.argv) < 2:
    print ("usage: ext_info.py path")
    print ("displays number of files and total size of files per extension in the specified path.")
    exit()

path_str = sys.argv[1]
folder = Path(path_str)

def suffix_info():
    return {
        'count': 0,
        'size': 0,
    }
suffixes = defaultdict(suffix_info)

files = [p for p in folder.iterdir() if p.is_file()]

for f in files:
    suf = f.suffix
    if len(suf) == 0:
        suf = '.'
    if suf != '.':
        suf = suf[1:]

    suffixes[suf]['count'] += 1
    suffixes[suf]['size'] += f.stat().st_size

for name, info in sorted(suffixes.items()):
    print (name, info['count'], info['size'])
