n = int(input())
for i in range(1, 21):
    for j in range(i, 21):
        if(n % (i + j) == 0 and i!=j):
           print ( i, j, sep='', end='')
