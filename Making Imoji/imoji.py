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
    glClearColor(0.0, 0.0, 0.0,0.0)
    glOrtho(-15, 15, -15, 15, -15, 5)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 3.0)
    glColor3f(1.0, .70, 0.0)
    imoji(10, 10, 0, 0)
    glColor3f(1.0,.80,0.0)
    imoji(9.5, 9.5, -.65, -.90)
    glColor3f(0.0, 0.0, 0.0)
    imoji(5.5, 5.0, -.70, -3.0)
    glColor3f(1.0,.80,0.0)
    imoji(6.5, 4.0, -.70, -0.15)
    glColor3f(1.0,0.0,0.0)
    imoji(2.5, 1, -.70, -7)
    glColor3f(0.0, 0.0, 0.0)
    imoji(2.5, 2.5, -4.5, 2.0)
    glColor3f(1.0, .80, 0.0)
    imoji(2.7, 2.5, -4.5, 1.5)
    glColor3f(0.0, 0.0, 0.0)
    imoji(1.5, 1.5, -4.5, 2.0)
    glColor3f(1.0, 1.0, 1.0)
    imoji(1.35, 1.35, -4.5, 2.0)
    glColor3f(0.0, 0.0, 0.0)
    imoji(0.70, 0.70, -4.3, 2.0)
    glColor3f(1.0, 1.0, 1.0)
    imoji(0.08, 0.08, -3.9, 2.0)
    glColor3f(0.0, 0.0, 0.0)
    imoji(2.5, 2.5, 4.0, 2.0)
    glColor3f(1.0, .80, 0.0)
    imoji(2.7, 2.5, 4.0, 1.5)
    glColor3f(0.0, 0.0, 0.0)
    imoji(1.5, 1.5, 4.0, 2.0)
    glColor3f(1.0, 1.0, 1.0)
    imoji(1.35, 1.35, 4.0, 2.0)
    glColor3f(0.0, 0.0, 0.0)
    imoji(0.70, 0.70, 4.2, 2.0)
    glColor3f(1.0, 1.0, 1.0)
    imoji(0.08, 0.08, 4.6, 2.0)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(200, 200)
wind = glutCreateWindow(" Md. Mehedi Hasan (163-15-8421)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()