from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def algorithm():
    def customround(M):
        n = M - .50
        if n % 2 == 0:
            M = math.ceil(M)
        else:
            M = round(M)
        return float(M)

    def highLowExchanger(x):
        if x < low:
            return True
        elif x > high:
            return True


    def DDA(x0, y0, x1, y1):
        x1 = float(x1)
        y1 = float(y1)
        gx1 = list()
        gy1 = list()
        cordination = list()
        xn = float(x0)
        yn = float(y0)
        m = (y1-y0)/(x1-x0)
        m =round(m,2)


        if 0 < m and m <= 1:
            xT = x0 + 1
            if highLowExchanger(xT):  # asdasdasdadasdasdas
                x0, x1, xn = x1, x0, x1
                y0, y1, yn = y1, y0, y1
            gx1.append(xn)
            gy1.append(yn)
            cordination.append((customround(xn), customround(yn)))
            while True:
                xn = x0 + 1
                yn = y0 + m
                gx1.append(xn)
                gy1.append(yn)
                cordination.append((customround(xn), customround(yn)))
                x0, y0 = xn, yn
                if xn >= x1 :
                    break
                else:
                    continue
        elif( -1<= m and m <= 0):

            xT = x0 - 1
            if highLowExchanger(xT): #asdasdasdadasdasdas
                x0, x1, xn = x1, x0, x1
                y0, y1, yn = y1, y0, y1
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
                if xn <= x1:   # =============== change < and > if infinity
                    break
                else:
                    continue
        elif (m > 1):
            xT = x0 + (1/m)
            if highLowExchanger(xT):  # asdasdasdadasdasdas
                x0, x1, xn = x1, x0, x1
                y0, y1, yn = y1, y0, y1
            gx1.append(xn)
            gy1.append(yn)
            cordination.append((customround(xn), customround(yn)))
            while True:
                x = x0 + (1/m)
                y = y0 + 1
                gx1.append(x)
                gy1.append(y)
                highLowExchanger(x)  # asdasdasdadasdasdas
                cordination.append((customround(x), customround(y)))
                x0, y0 = x, y
                if x >= x1:
                    break
                else:
                    continue

        elif(m < -1):
            xT = x0 - (1 / m)

            if highLowExchanger(xT):  # asdasdasdadasdasdas
                x0, x1, xn = x1, x0, x1
                y0, y1, yn = y1, y0, y1
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
                if x >= x1:
                    break
                else:
                    continue
        return gx1, gy1, cordination


    x1, y1, x2, y2 = 80, 320, 200, 30
    if(x2 - x1 < 0):
        low = x2
        high = x1
    else:
        low = x1
        high = x2

    xnew1,ynew1, Ncordination = DDA(x1, y1, x2, y2)
    return Ncordination




def display():
    algo = algorithm()
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    for i in algo:
        glVertex2f(i[0], i[1])
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,300 , 0.0, 300, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 3.0)
    display()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 600)
glutInitWindowPosition(150, 10)
wind = glutCreateWindow(" Md. Mehedi Hasan (163-15-8421)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()