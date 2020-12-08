import math as m
from termcolor import colored

x = [p*2 for p in [4, 6, 4, 6] ] #.....................
y = [p*2 for p in [9, 9, 11, 11] ]
# x = [p*2 for p in [5, 7, 5, 7] ] #.....................
# y = [p*2 for p in [6, 6, 8, 8] ]  #.....................
print(x,y)
xP = []
yP = []
Len = len(x)

print(colored("=========================translation============", 'blue'))

for i in range(Len):
    print("({},{})".format(x[i], y[i]), end=' ')
print()

tx = 1  #.....................
ty = 1  #.....................

for i in range(Len):
    xP.append(x[i]+tx)
    yP.append(y[i]+ty)

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{})".format(xP[i], yP[i]), end=' ')
print()
print()
print()





print(colored("=========================Shearing============", 'blue'))

for i in range(Len):
    print("({},{})".format(x[i], y[i]), end=' ')
print()

shy = -1  #.....................
xP = []
yP = []
for i in range(Len):
    xP.append(x[i])
    yP.append(y[i]+(shy*x[i]))

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{})".format(xP[i], yP[i]), end=' ')
print()
print()
print()



print(colored("=========================rotation============", 'blue'))

for i in range(Len):
    print("({},{})".format(x[i], y[i]), end=' ')
print()

theta = m.radians(30)  #.....................
C_W = 1     # 1 if clock wise 0 if anti clock wise
xP = []
yP = []

if C_W:
    print(colored("                                      clock wise", 'red'))
else:
    print(colored("                                      anti clock wise", 'red'))
for i in range(Len):
    if C_W:
        # print(m.cos(theta))
        # print(m.sin(theta))
        xP.append(
            x[i] * m.cos(theta) + y[i] * m.sin(theta)
        )
        yP.append(
            -x[i] * m.sin(theta) + y[i] * m.cos(theta)
        )
    else:
        xP.append(
            x[i] * m.cos(theta) - y[i] * m.sin(theta)
        )
        yP.append(
            x[i] * m.sin(theta) + y[i] * m.cos(theta)
        )

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({:.2f},{:.2f})".format(xP[i], yP[i]), end=' ')
print()
print()
print()





print(colored("=========================Scaling============", 'blue'))


for i in range(Len):
    print("({},{})".format(x[i], y[i]), end=' ')
print()

sx = 2  #.....................
sy = 2  #.....................
xP = []
yP = []
for i in range(Len):
    xP.append(x[i] * sx)
    yP.append(y[i] * sy)

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{})".format(xP[i], yP[i]), end=' ')
print()
print()
print()





print(colored("=========================Reflection============", 'blue'))



for i in range(Len):
    print("({},{})".format(x[i], y[i]), end=' ')
print()

theta = 30  #.....................
X_A = 0     # 1 if X AXIS 0 if Y AXIS
xP = []
yP = []
if X_A:
    print(colored("                                      x axis", 'red'))
else:
    print(colored("                                      y axis", 'red'))

for i in range(Len):
    if X_A:
        xP.append(x[i])
        yP.append(-y[i])
    else:
        xP.append(-x[i])
        yP.append(y[i])

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({:.2f},{:.2f})".format(xP[i], yP[i]), end=' ')
print()
print()
print()
