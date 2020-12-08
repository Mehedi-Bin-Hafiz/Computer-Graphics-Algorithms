# x1, y1, x2, y2 =  27, 41, 18, 35,
x1, y1, x2, y2 = 5, 8, 2, 9

if(x2 - x1 <= 0):
    x1, x2 = x2, x1
    y1, y2 = y2, y1

dx = x2-x1
dy = y2-y1
p0 = 2*dy - dx
print('dx : ', dx)
print('dy : ', dy)
print('p0 : ', p0)
a = ' \t'
print('=========== Co-ords Values============')
print(' p\t   x\t  y\t     (x,y)')
print(' {:}     {:}     {:}     ({},{})'.format(p0, x1, y1, x1, y1))

while True:
    if p0 < 0:
        p0 = p0 + 2*dy
        x1 += 1
        print(' {:}     {:}     {:}     ({},{})'.format(p0, x1, y1, x1, y1))
    elif p0 >= 0:
        p0 = p0 + (2*dy - 2*dx)
        x1 += 1
        y1 += 1
        if p0 < 0:
            print('{:}     {:}     {:}     ({},{})'.format(p0, x1, y1, x1, y1))
        else:
            print(' {:}     {:}     {:}     ({},{})'.format(p0, x1, y1, x1, y1))
    if x1 == x2:
        break
