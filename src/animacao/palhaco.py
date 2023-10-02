import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(900, 900)
        glutCreateWindow(b"palhaco")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutDisplayFunc(self.display)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glOrtho(-7, 7, -7, 7, -7, 7)
        glPushMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.draw_sphere(0.5, 50, 50)

        glTranslatef(1, 1, 0.0)
        glColor3f(1.0, 0.0, 0.0)
        self.draw_cone(0.4, 0.4, 50, 50)

        glFlush()

    def draw_sphere(self, radius, slices, stacks):
        quad = gluNewQuadric()
        gluSphere(quad, radius, slices, stacks)

    def draw_cone(self, base, height, slices, stacks):
        quad = gluNewQuadric()
        gluCylinder(quad, base, 0, height, slices, stacks)

if __name__ == "__main__":
    app = App()
    glutMainLoop()
