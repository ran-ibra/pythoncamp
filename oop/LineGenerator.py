from typing import Iterator, Iterable, Tuple, List

def readlines(filename: str, encoding: str = "utf-8") :
    with open(filename, "r", encoding=encoding) as f:
        for line in f:
            yield line
iteratfile=readlines('3.txt')
print(iteratfile.__next__())
print(iteratfile.__next__())

def filter_lines(lines, keyword: str):
    for line in lines:
        if keyword in line:
            yield line
# print(f.__next__())
def striplines(lines):
    for line in lines:
        yield line.strip()
strp= striplines(iteratfile)
f= filter_lines(strp, "virtual")
print(f)
# print(iteratfile.__next__())
def number_lines(lines, start= 1):
    n = start
    for line in lines:
        yield f"{n}: {line}"
        n += 1
print(number_lines(strp))


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

filtered = filter_lines(cleaned, "virtual")

numbered = number_lines(filtered)

chunks = chunk_lines(cleaned, 4)

for chunk in chunks:
    print("CHUNK:")
    for line in chunk:
        print("   ", line)