
""" input r all time """
r = 16
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
cx = 5
cy = 8


print('=========== Co-ords Values============')
print('k      p\t    Xk+1  Yk+1\t   (x, y)')
# print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k,p0, x, y, x+cx, y+cy))


while True:

    if p0 < 0:


        x += 1
        y = y
        print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k, p0, x , y, x + cx, y + cy))
        p0 = p0 + 2 * x + 3

    elif p0 >= 0:


        x += 1
        y -= 1
        print('{:<3}    {:<5}     {:}     {:}     ({},{})'.format(k, p0, x, y, x + cx, y + cy))
        p0 = p0 + (2 * x + 5) - (2 * y)
    k += 1
    if x >= y:
        break


