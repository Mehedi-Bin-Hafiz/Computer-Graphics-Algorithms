from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def algorithm():
    x1, y1, x2, y2 = 80, 320, 200, 30
    cordinates = list()
    if(x2 - x1 <= 0):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = x2-x1
    dy = y2-y1
    p0 = 2*dy - dx
    cordinates.append([x1,y1])
    while True:
        if p0 < 0:
            p0 = p0 + 2*dy
            x1 += 1
            cordinates.append([x1, y1])
        elif p0 >= 0:
            p0 = p0 + (2*dy - 2*dx)
            x1 += 1
            y1 += 1
            cordinates.append([x1, y1])

        if x1 == x2:
            break
    return cordinates

algo = algorithm()
print(algo)
def display():

    algo = algorithm()
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)
    for i in algo:
        glVertex2f(i[0], i[1])
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
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
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()