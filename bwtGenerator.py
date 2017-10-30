def get_bwt(line):
    array = []
    for i in range(len(line)):
        st = line[i:] + line[0:i]  # generating cyclic rotations
        array.append(st)
    array.sort()  # sorting the cyclic rotations according to unicode values

    bwt = []
    for i in range(len(array)):
        bwt.append(array[i][-1])
    return bwt


def compress(bwt):
    encoded = ""
    count = 0
    prevChar = bwt[0]
    for char in bwt:
        if char == prevChar:
            count += 1
        else:
            encoded = encoded + str(count) + prevChar
            output.write(str(count) + " " + prevChar + "\n")
            prevChar = char
            count = 1
    output.write(str(count) + " " + char + "\n")
    encoded = encoded + str(count) + char
    print(encoded)
    return encoded


infile = open('text.txt')
output = open('exam.bz2', 'w')

line = ""
for item in infile:
    line = line + item

line = line.replace('\n', '-')
line = line.replace(' ', '*')
bwt = get_bwt(line + '$')
b = ""
for i in bwt:
    b += i
print(b)


compressed = compress(bwt)
print(len(bwt), len(compressed))
output.close()
