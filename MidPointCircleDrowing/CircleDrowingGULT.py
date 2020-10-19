from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def algorithm():
    """ input r all time """
    r = 16
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
    cx = 5
    cy = 8
    cordination = list()
    while True:

        if p0 < 0:
            p0 = p0 + 2 * x + 3
            x += 1
            y = y
            cordination.append([x + cx, y + cy])


        elif p0 >= 0:
            p0 = p0 + (2 * x + 5) - (2 * y)
            x += 1
            y -= 1
            cordination.append([x + cx, y + cy])

        k += 1
        if x >= y:
            break
    return cordination


# algo = algorithm()
# glBegin(GL_QUADS)
# for i in algo:
#     print(i[0], i[1])
# glEnd()

def display():
    algo = algorithm()
    print(algo)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    for i in algo:
        print(i[0], i[1])
        glVertex2f(i[0], i[1])
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 10, -10)
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