a = input()
k = 0 
b = [str(x) for x in a.split()]
for i in range(len(b)):
    if b[i][0] == 'е':
        k = k + 1 
print(k)