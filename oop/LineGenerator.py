from typing import Iterator, Iterable, Tuple, List

def readlines(filename: str, encoding: str = "utf-8") :
    with open(filename, "r", encoding=encoding) as f:
        for line in f:
            yield line
iteratfile=readlines('3.txt')
print("All lines:")
for line in readlines('3.txt'):
    print(repr(line))

def filter_lines(lines, keyword: str):
    for line in lines:
        if keyword in line:
            yield line
def striplines(lines):
    for line in lines:
        yield line.strip()
strp= striplines(iteratfile)
for i in strp:
    print(i)
f= filter_lines(iteratfile,"python")
for line in f:
    print(line)
# print(f.__next__())



# print(iteratfile.__next__())
def number_lines(lines, start= 1):
    n = start
    for line in lines:
        yield n, line
        n += 1
nummm=number_lines(f)
for i in nummm:
    print(i)


def chunk_lines(lines, chunk_size) :

    if chunk_size <= 0:
        raise ValueError("chunk_size must be >= 1")
    chunk: List[str] = []
    for line in lines:
        chunk.append(line)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
chunk_lines(iteratfile,2)

iterfile = readlines('3.txt')

cleaned = striplines(iterfile)
chunks = chunk_lines(cleaned, 2)

for chunk in chunks:
    print("CHUNK:")
    for line in chunk:
        print("   ", line)