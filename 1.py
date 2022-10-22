n = int(input())
array = [float(i) for i in input().split()]
imin = 0
imax = 0
def 
for i in range(1, n):
    if (array[i] >= array[imin]):
        imin = i
for i in range (imin + 1, n):
    if (array[i] >= array[imax]):
        imax = i
for i in range (imax + 1, n):
    array[i] = 0
print(array)
