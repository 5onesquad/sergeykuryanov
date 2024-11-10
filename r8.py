q = input('Площадь какой фигуры ищем(т-треугольник,п-прямоугольник):')
if q == 'т':
    a = int(input('высота'))
    b = int(input('основание'))
s = (1/2) * a * b
if q == 'п':
    a = int(input('длина'))
    b = int(input('ширина'))
print('s')

a = []
b = []
c = []
s = 0 
for i in range(len(a)):
    s = s + a[i]
print(s,s/len(a))

for i in range(len(b)):
    s = s + b[i]
print(s,s/len(b))

for i in range(len(c)):
    s = s + c[i]
print(s,s/len(c))