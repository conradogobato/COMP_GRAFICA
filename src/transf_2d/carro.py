import math
from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.ang = 2
        self.theta = 0
        self.cor_vetor = [[0,0,1],[1,0,0],[0,1,0],[1,1,0],[0,1,1],[1,0,1],[1,1,1],[0,0,1],[1,0,1],[1,0,1]]
        self.right = 0
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
        glTranslate(self.right, 0.0, 0.0)
        glPushMatrix()
        glScale(1.5, 0.7, 1.0)
        self.carro()

        glPopMatrix()
        glPushMatrix()
        glScale(0.090, 0.090, 1)
        glTranslatef(1.5, -2.0, 0.0)
        glRotate(self.theta, 0.0, 0.0, 1.0)
        self.rodas()


        glPopMatrix()
        glScale(0.090, 0.090, 1)
        glTranslatef(-1.5, -2.0, 0.0)
        glRotate(self.theta, 0.0, 0.0, 1.0)
        self.rodas()

        glPopMatrix()

    def rodas(self):
        glBegin(GL_POINTS)
        for i in range(10):
            glColor3fv(self.cor_vetor[i])
            glVertex2f(0.5*math.cos(self.ang),0.5*math.sin(self.ang))
            self.ang = self.ang+(2*math.pi)/10
        glEnd()
        glFlush()

    def carro(self):
        glBegin(GL_POLYGON)
        glVertex2d(-0.15, 0.15)
        glVertex2d(0.15, 0.15)
        glVertex2d(0.15, -0.15)
        glVertex2d(-0.15, -0.15)
        glEnd()
        glFlush()
        

    def mouse_click(self, button, state, x, y):
        pass

    def keyboard(self, key, x, y):
        self.key_pressed = key
        if self.key_pressed == b'd':
            self.right+=0.01
            self.theta-=20
        if self.key_pressed == b'a':
            self.right-=0.01
            self.theta+=20
        glutPostRedisplay()

if __name__ == "__main__":
    App()
