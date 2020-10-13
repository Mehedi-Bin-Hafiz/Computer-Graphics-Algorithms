import time
import math

def customround(M):
    n = M - .50
    if n % 2 == 0:
        M = math.ceil(M)
    else:
        M = round(M)
    return float(M)


def DDA(x0,y0,x1,y1):
    x1 = float(x1)
    y1 = float(y1)
    gx1=list()
    gy1=list()
    cordination=list()
    xn= float(x0)
    yn= float(y0)
    m = (y1-y0)/(x1-x0)
    m =round(m,2)

    print("The value of m is= ",m)
    if 0 < m and m <= 1:
        gx1.append(xn)
        gy1.append(yn)
        cordination.append((customround(xn), customround(yn)))
        while True:
            xn = x0 + 1
            yn = y0 + m
            gx1.append(xn)
            gy1.append(yn)
            cordination.append((customround(xn), customround(yn)))
            x0, y0 = xn,yn
            if xn == x1 :
                break
            else:
                continue
    elif( -1<= m and m <= 0):
        if(x0>x1 and y0>y1):
            temp=xn
            xn=x1
            x1=temp
            temp2=yn
            yn=y1
            y1=temp2
        gx1.append(xn)
        gy1.append(yn)
        cordination.append((customround(xn), customround(yn)))
        while True:
            xn = x0 - 1
            yn = y0 - m
            gx1.append(xn)
            gy1.append(yn)
            cordination.append((customround(xn), customround(yn)))
            x0, y0 = xn, yn
            if xn == x1 or yn == y1:
                break
            else:
                continue
    elif (m > 1):
        gx1.append(xn)
        gy1.append(yn)
        cordination.append((customround(xn), customround(yn)))
        while True:
            x = x0 + (1/m)
            y = y0 + 1
            gx1.append(x)
            gy1.append(y)
            cordination.append((customround(x), customround(y)))
            x0, y0 = x, y
            if x == x1 :
                break
            else:
                continue

    elif(m < -1):
        if (x0 > x1 and y0 > y1):
            temp = xn
            xn = x1
            x1 = temp
            temp2 = yn
            yn = y1
            y1 = temp2
        gx1.append(xn)
        gy1.append(yn)
        cordination.append((customround(xn), customround(yn)))
        while True:
            x = x0 - (1 / m)
            y = y0 - 1
            gx1.append(x)
            gy1.append(y)
            cordination.append((customround(x), customround(y)))
            x0, y0 = x, y
            if xn == x1 or yn == y1:
                break
            else:
                continue
    return gx1, gy1, cordination


""" x0,y0,x1,y1 """
#xnew1,ynew1, Ncordination = DDA(15,27,26,33)
#xnew1,ynew1, Ncordination = DDA(32,16,37,26)
xnew1,ynew1, Ncordination = DDA(15,5,5,10)


print("x1         y1         (x1,y1)")
for i in range(0,len(xnew1)):
    print("{:.2f}  -> {:>.2f} ->    {}".format(xnew1[i], ynew1[i],Ncordination[i]))


