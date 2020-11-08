from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def imoji(rx,ry,cx,cy):

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx,cy)

    for i in range(0,101):
        angle = 2.0 * 3.1416 * i/100
        x = rx * math.cos(angle)
        y = ry * math.sin(angle )
        glVertex2f((x+cx),(y+cy))
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0,1.0)
    glOrtho(-15, 15, -15, 15, -15, 5)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 3.0)
    glColor3f(0.0, 0.0, 0.0)
    imoji(10, 10, 0, 0)
    glColor3f(1.0,1.0,1.0)
    imoji(9.5, 9.5, .60, 2)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(20, 20)
wind = glutCreateWindow(" Md. Mehedi Hasan (163-15-8421)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()