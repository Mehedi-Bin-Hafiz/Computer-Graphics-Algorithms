
""" input r all time """
r = 6
if isinstance(r, float):
    p0 = (5/4) - r
else:
    p0 = 1 - r
print("p0= ", p0)

""" initial cordinaltion """
#######Fixed######
x = 0
y = r
k = 0
#######Fixed######

###### Center value (if given then change) ######
cx = 2
cy = 9


print('=========== Co-ords Values============')
print('k      p\t    Xk+1  Yk+1\t   (x, y)')
# print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k,p0, x, y, x+cx, y+cy))


while True:

    if p0 < 0:
        print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k, p0, x+1 , y, x + cx+1, y + cy))
        p0 = p0 + 2 * x + 3
        x += 1
        y = y


    elif p0 >= 0:
        print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k, p0, x+1, y-1, x + cx+1, y + cy-1))
        p0 = p0 + (2 * x + 5) - (2 * y)
        x += 1
        y -= 1

    k += 1
    if x >= y:
        break


