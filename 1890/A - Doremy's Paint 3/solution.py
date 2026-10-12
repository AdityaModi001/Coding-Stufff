# the array is good if the sum of the adjecnt elemets of the array has the sum equal
from collections import Counter
import sys
t = int(sys.stdin.readline())
 
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
 
    freq = Counter(a)
    if len(freq) >= 3:
        print('NO')
    else:
        # getting the frequency of the smallest and the laragest element
        fre1_1  = next(iter(freq.values()))
        freq_2 = list(freq.values())[-1]
 
        if fre1_1 == freq_2:
            print('YES')
        elif n % 2 == 1 and abs(fre1_1 - freq_2) == 1:
            print("Yes")
        else:
            print('No')
 