from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def algorithm():
    """ input r all time """
    r = 11
    if isinstance(r, float):
        p0 = (5 / 4) - r
    else:
        p0 = 1 - r

    """ initial cordinaltion """
    #######Fixed######
    x = 0
    y = r
    k = 0
    #######Fixed######

    ###### Center value (if given then change) ######
    cx = -5
    cy = 7
    cordination = list()
    while True:

        if p0 < 0:
            cordination.append([x + cx + 1, y + cy])
            p0 = p0 + 2 * x + 3
            x += 1
            y = y


        elif p0 >= 0:
            cordination.append([x + cx + 1, y + cy - 1])
            p0 = p0 + (2 * x + 5) - (2 * y)
            x += 1
            y -= 1
        k += 1
        if x >= y:
            break
    return cordination


def display():
    algo = algorithm()
    print(algo)

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    for i in algo:
        glVertex2f(i[0], i[1])
    glEnd()


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-25, 50, -25, 50, 0.0, 1.0)
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