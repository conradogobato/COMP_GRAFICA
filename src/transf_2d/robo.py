import math
from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.theta = 0
        self.ang = 10
        self.times_theta = 0
        self.times_gama = 0
        self.gama = 0
        self.key_pressed = b''  # Inicialize a variável de tecla pressionada
        self.init_window()

    def normalize_x(self, x):
        return ((x / 200.0) - 1.0)

    def normalize_y(self, y):
        return (-(y / 200.0) + 1.0)

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(900, 900)
        glutCreateWindow(b"Desenhar Ponto no Clique do Mouse")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse_click)
        glutKeyboardFunc(self.keyboard)
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(2.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()
        

        glColor3f(0,0,1)
        glTranslate(0,0.37,0)
        glScale(0.2, 0.2, 1.0)
        self.cabeca()

        glPopMatrix()
        glPushMatrix()

        glColor3f(0,0,1)
        glScale(0.4, 1.8, 1.0)
        self.robo()

        glPopMatrix()
        glPushMatrix()


        #BRAÇOS
        glColor3f(0,0,1)
        glRotate(self.theta, 0, 0, 1)
        glTranslate(0.2, 0.0, 0.0)
        glRotate(45, 0, 0, 1)
        
        glScale(0.4, 1.8, 1.0)
        self.robo()

        glPopMatrix()
        glPushMatrix()

        glColor3f(0,0,1)
        glRotate(-self.theta, 0, 0, 1)
        glTranslate(-0.2, 0.0, 0.0)
        glRotate(-45, 0, 0, 1)
        
        glScale(0.4, 1.8, 1.0)
        self.robo()

        glPopMatrix()
        glPushMatrix()


        #PERNAS
        glColor3f(0,0,1)
        glTranslate(0.15, -0.4, 0)
        glRotate(30, 0, 0, 1)
        glRotate(self.gama, 0, 0, 1)
        glScale(0.4, 1.8, 1.0)
        self.robo()


        glPopMatrix()
        glPushMatrix()

        glColor3f(0,0,1)
        glTranslate(-0.15, -0.4, 0)
        glRotate(-30, 0, 0, 1)
        glRotate(-self.gama, 0, 0, 1)
        glScale(0.4, 1.8, 1.0)
        self.robo()

        glPopMatrix()



    def robo(self):
        glBegin(GL_POLYGON)
        glVertex2d(-0.15, 0.15)
        glVertex2d(0.15, 0.15)
        glVertex2d(0.15, -0.15)
        glVertex2d(-0.15, -0.15)
        glEnd()
        glFlush()
    
    def cabeca(self):
        glBegin(GL_POINTS)
        for i in range(400):
            glVertex2f(0.5*math.cos(self.ang),0.5*math.sin(self.ang))
            self.ang = self.ang+(2*math.pi)/400
        glEnd()
        glFlush()
        

    def mouse_click(self, button, state, x, y):
        pass

    def keyboard(self, key, x, y):
        self.key_pressed = key
        if self.key_pressed == b'b':
            if self.times_theta == 0:
                self.theta+=20
                self.times_theta+=1
            else:
                self.theta-=20
                self.times_theta-=1
        if self.key_pressed == b'p':
            if self.times_gama == 0:
                self.gama+=20
                self.times_gama+=1
            else:
                self.gama-=20
                self.times_gama-=1
        glutPostRedisplay()

if __name__ == "__main__":
    App()
