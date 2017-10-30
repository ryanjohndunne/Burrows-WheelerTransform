# Burrows-Wheeler Transform
Use Burrows-Wheeler transform to compress and decompress text.

# bwtGenerator.py
Given an input file named 'text.txt' bwtGenerator will create the Burrows-Wheeler transform for this text. Once this has been completed the BWT will be compress like the following:

If BWT is = aaaabbbbdddcc, then:

Output will be: a4b4d3c2

This output is then saved to "exam.bz2"

#bwtDecompress.py
Given the compressed Burrors-Wheeler transform the program will decompress it into the full BWT and using the BWT, it will reproduce the original text to print. It does this as follows:
1. Take the decompressed BWT and create a duplicate.
2. Using radix sort we sort the duplicate BWT in order by it's unicode values, while also making note of it's occurence across all other identicle letters, using radix sort - this lets us sort symbols as well as letters.
3. Using the sorted BWT and the original BWT we follow the logic of the BWT inversion algorithm which is:

original word = $banana
sortedList = $, a, a, a, b, n, n,
BWT = b, n, n, $, a, a, a
string = "$"

SortedList    BWT

$      ->       b 1. add b to string. String = "$b" go to first occurance of b in sorted list

a      ->       n 3. add n to string. String = "$ban" go to first occurance of n

a      ->       n 5. add n to string. String = "$banan" go to second occurance of n

a      ->       $ 6. $ denotes end of the string, we're finished

b      ->       a 2. add a to string. String = "$ba" go to the first occurance of a

n      ->       a 4. add a to string. String = "$bana" go to second occurance of a

n      ->       a 5. add a to string. String = "$banana" go to third occurance of a

string is now set to "$banana". This is how we generate the original word from BWT using the inverse.

Time complexity = O(M + N) Where M is the size of the alphabet (255 for unicode) and N is the length of the original decompressed text.

Space complexity = O(M + N) Where M is the size of the alphabet (255 for unicode) and N is the length of the original decompressed text.
