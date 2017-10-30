LEN_OF_UNICODE = 255


class Letter(object):
    def __init__(self, letter=None, occurrence=None):
        self.letter = letter
        self.occurrence = occurrence


def radixSort(aList):
    """
    Sort a list of characters by it's unicode value
    Time complexity: O(N)
    Space complexity: O(N)
    """
    RADIX = LEN_OF_UNICODE
    Rank = [[]]
    BWT = []

    buckets = [[] for _ in range(RADIX)]

    for i in aList:
        buckets[ord(i)].append(i)
        letter = Letter()
        letter.letter = i
        letter.occurrence = len(buckets[ord(i)])
        BWT.append(letter)

    # merge all the buckets into aList in sorted order
    a = 0
    for b in range(RADIX):
        buck = buckets[b]
        for i in range(len(buck)):
            letter = Letter()
            letter.letter = buck[i]
            letter.occurrence = i + 1

            aList[a] = letter

            # Row number of the first occurrence of each character
            if letter.occurrence == 1:
                Rank.append([a, letter])

            a += 1

    return aList, BWT, Rank


# Reads in the file titled 'exam.bz2'
# storing it in the BWT array and returning it
def getBWT():
    BWT = []
    f = open('exam.bz2', 'r')

    for line in f:
        line.rstrip()
        line = line.split()
        for i in range(int(line[0])):
            BWT.append(line[1])

    return BWT


# Convert BWT into the decompressed text
def inversion(BWT, sortedBWT, Rank):
    row = 0
    string = ""
    for i in range(len(BWT)):
        # The letter/character we are currently using
        character = BWT[row].letter
        # returns what occurrence this number is
        charOccurrence = BWT[row].occurrence

        if character == '*':
            string = ' ' + string
        elif character == '-':
            string = '\n' + string
        elif character == '$':
            pass
        else:
            string = character + string

        for i in range(len(Rank)):
            if Rank[i][1].letter == character:
                charRank = Rank[i][0]
                break

        row = charRank + charOccurrence - 1

    print(string)


def main():
    BWT = getBWT()  # Builds the BWT
    # returns sorted BWT, BWT and the first position of each char
    sortedBWT, BWT, Rank = radixSort(BWT)
    del Rank[0]     # Rank[0] is always empty
    # prints the decompressed string built using the BWT
    inversion(BWT, sortedBWT, Rank)


main()
