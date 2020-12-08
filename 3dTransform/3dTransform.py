import math as m
from termcolor import colored

# x =[4, 6, 4, 6] #.....................
# y = [9, 9, 11, 11]
# z = [5, 7, 8, 11]
# x = [0, 1, 1] #.....................
# y = [0, 1, 1] #.....................
# z = [0, 2, 3]
x = [0, 3, 3] #.....................
y = [3, 3, 0] #.....................
z = [1, 2, 0]

print(x, y)
xP = []
yP = []
zP = []
Len = len(x)

print(colored("=========================translation============", 'blue'))

for i in range(Len):
    print("({},{},{})".format(x[i], y[i], z[i]), end=' ')
print()

tx = 1  #.....................
ty = 1  #.....................
tz = 2  #.....................

for i in range(Len):
    xP.append(x[i]+tx)
    yP.append(y[i]+ty)
    zP.append(z[i]+tz)

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{},{})".format(xP[i], yP[i], zP[i]), end=' ')
print()
print()
print()





print(colored("=========================Shearing============", 'blue'))

for i in range(Len):
    print("({},{},{})".format(x[i], y[i], z[i]), end=' ')
print()

shx = 2  #.....................
shy = 2  #.....................
shz = 3  #.....................
xP = []
yP = []
zP = []
for i in range(Len):
    # ======================== x axis
    xP.append(x[i])
    yP.append(y[i]+(shy*x[i]))
    zP.append(z[i]+(shz*x[i]))

    #======================== y axis
    # xP.append(x[i]+(shx*x[i]))
    # yP.append(y[i])
    # zP.append(z[i]+(shz*x[i]))

    #======================== z axis
    # xP.append(x[i]+(shx*x[i]))
    # yP.append(y[i]+(shy*x[i]))
    # zP.append(z[i])

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{},{})".format(xP[i], yP[i], zP[i]), end=' ')
print()
print()
print()



print(colored("=========================rotation============", 'blue'))

for i in range(Len):
    print("({},{},{})".format(x[i], y[i], z[i]), end=' ')
print()

theta = m.radians(90)  #.....................
C_W = 1     # 1 if clock wise 0 if anti clock wise
xP = []
yP = []
zP = []

if C_W:
    print(colored("                                      clock wise", 'red'))
else:
    print(colored("                                      anti clock wise", 'red'))
for i in range(Len):
    if C_W:
        # print(m.cos(theta))
        # print(m.sin(theta))
        #=========================================== x-axis
        # xP.append(x[i])
        # yP.append(
        #     y[i] * m.cos(theta) - z[i] * m.sin(theta)
        # )
        # zP.append(
        #     y[i] * m.sin(theta) + z[i] * m.cos(theta)
        # )

        # =========================================== y-axis
        '''
        yP.append(y[i])
        xP.append(
            x[i] * m.cos(theta) + z[i] * m.sin(theta)
        )
        zP.append(
            z[i] * m.cos(theta) - x[i] * m.sin(theta)
        )
        '''
        # =========================================== z-axis
        # '''
        zP.append(z[i])
        xP.append(
            x[i] * m.cos(theta) - y[i] * m.sin(theta)
        )
        yP.append(
            x[i] * m.sin(theta) + y[i] * m.cos(theta)
        )
        # '''



    else:
        xP.append(
            x[i] * m.cos(theta) - y[i] * m.sin(theta)
        )
        yP.append(
            x[i] * m.sin(theta) + y[i] * m.cos(theta)
        )

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({:.2f},{:.2f},{:.2f})".format(xP[i], yP[i], zP[i]), end=' ')
print()
print()
print()





print(colored("=========================Scaling============", 'blue'))


for i in range(Len):
    print("({},{},{})".format(x[i], y[i], z[i]), end=' ')
print()

sx = 2  #.....................
sy = 3  #.....................
sz = 3  #.....................
xP = []
yP = []
zP = []
for i in range(Len):
    xP.append(x[i] * sx)
    yP.append(y[i] * sy)
    zP.append(z[i] * sz)

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({},{},{})".format(xP[i], yP[i], zP[i]), end=' ')
print()
print()
print()





print(colored("=========================Reflection============", 'blue'))



for i in range(Len):
    print("({},{},{})".format(x[i], y[i], z[i]), end=' ')
print()

theta = 30  #.....................
X_A = 0     # 1 if X AXIS ======== 0 if Y AXIS ====== 2 z axis
xP = []
yP = []
zP = []
if X_A == 1:
    print(colored("                                      x axis", 'red'))
elif X_A == 2:
    print(colored("                                      z axis", 'red'))
else:
    print(colored("                                      y axis", 'red'))

for i in range(Len):
    if X_A == 1:
        xP.append(x[i])
        yP.append(-y[i])
        zP.append(-z[i])
    if X_A == 2:
        xP.append(-x[i])
        yP.append(-y[i])
        zP.append(z[i])
    else:
        xP.append(-x[i])
        yP.append(y[i])
        zP.append(-z[i])

print(colored("                       >>>>>>>>>new cords=====", 'green'))
for i in range(Len):
    print("({:.2f},{:.2f},{:.2f})".format(xP[i], yP[i], zP[i]), end=' ')
print()
print()
print()
