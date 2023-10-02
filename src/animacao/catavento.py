import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.theta = 0
        self.vel = 50
        self.ang = 2
        self.key_pressed = b''  # Inicialize a variável de tecla pressionada
        self.init_window()
        

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(900, 900)
        glutCreateWindow(b"Catavvento")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse_click)
        glutKeyboardFunc(self.keyboard)
        glutTimerFunc(self.vel, self.anima, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluOrtho2D(0, 900, 0, 900) 
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(1.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glPushMatrix()

        glScalef(0.5, 0.5, 1.0)
        self.rosa()

        glPopMatrix()
        glPushMatrix()


        glScalef(0.38, 0.38, 1.0)
        glRotate(self.theta, 0, 0, 1)
        glPushMatrix()
        glTranslatef(0.9,0.9,0.0)
        self.rosa()


        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.9,-0.9,0.0)
        self.rosa()

        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.9,0.9,0.0)
        self.rosa()

        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.9,-0.9,0.0)
        self.rosa()

        glPopMatrix()
        glPopMatrix()

    def rosa(self):
        glBegin(GL_POINTS)
        for i in range(200):
            glVertex2f(0.5*math.cos(self.ang),0.5*math.sin(self.ang))
            self.ang = self.ang+(2*math.pi)/200
        glEnd()
        glFlush()

    def anima(self, value):
        self.theta+=2
        glutPostRedisplay()
        glutTimerFunc(self.vel,self.anima,1)

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            while(self.vel>1):
                self.vel -= 5
                time.sleep(0.05)
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            while(self.vel<50):
                self.vel += 5
                time.sleep(0.05)
                
            

    def keyboard(self, key, x, y):
        self.key_pressed = key
        if self.key_pressed == b'd':
            if self.vel > 1:
                self.vel-=5
        if self.key_pressed == b's':
            self.vel+=5
        glutPostRedisplay()

if __name__ == "__main__":
    App()
