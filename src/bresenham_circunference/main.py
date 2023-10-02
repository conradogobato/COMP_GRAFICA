from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.mouseX = 200.0
        self.raio_bool = True
        self.mouseY = 200.0
        self.point_size = 1.0
        self.raio = 50.0
        self.x = 0.0
        self.y = self.raio
        self.key_pressed = b''  # Inicialize a variável de tecla pressionada
        self.init_window()

    def normalize_x(self, x):
        return ((x / 200.0) - 1.0)

    def normalize_y(self, y):
        return (-(y / 200.0) + 1.0)

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(400, 400)
        glutCreateWindow(b"Desenhar Ponto no Clique do Mouse")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse_click)
        glutKeyboardFunc(self.keyboard)
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(self.point_size)
        self.x = 0
        self.y = self.raio
        pk = 5 / 4 - self.raio
        while (self.x <= self.y):
            if (pk < 0):
                pk = pk + 2 * self.x + 3
            else:
                pk = pk + 2 * (self.x - self.y) + 5
                self.y -= 1
            self.x += 1
            glBegin(GL_POINTS)
            glVertex2f(self.normalize_x(self.x + self.mouseX), self.normalize_y(self.y + self.mouseY))
            glVertex2f(self.normalize_x(self.mouseX - self.x), self.normalize_y(self.mouseY + self.y))
            glVertex2f(self.normalize_x(self.mouseX + self.x), self.normalize_y(self.mouseY - self.y))
            glVertex2f(self.normalize_x(self.mouseX - self.x), self.normalize_y(self.mouseY - self.y))
            glVertex2f(self.normalize_x(self.mouseX + self.y), self.normalize_y(self.mouseY + self.x))
            glVertex2f(self.normalize_x(self.mouseX - self.y), self.normalize_y(self.mouseY + self.x))
            glVertex2f(self.normalize_x(self.mouseX + self.y), self.normalize_y(self.mouseY - self.x))
            glVertex2f(self.normalize_x(self.mouseX - self.y), self.normalize_y(self.mouseY - self.x))
            glEnd()
            glFlush()

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.mouseX = x
            self.mouseY = y
            glutPostRedisplay()

    def keyboard(self, key, x, y):
        self.key_pressed = key
        if self.key_pressed == b'r':
            self.raio_bool = True
        if self.key_pressed == b't':
            self.raio_bool = False
        if self.key_pressed == b'1':
            if self.raio_bool:
                self.raio = 30.0
            else:
                self.point_size = 1.0
        if self.key_pressed == b'2':
            if self.raio_bool:
                self.raio = 40.0
            else:
                self.point_size = 5.0
        if self.key_pressed == b'3':
            self.raio = 50.0
        if self.key_pressed == b'4':
            self.raio = 60.0
        if self.key_pressed == b'5':
            self.raio = 70.0
        if self.key_pressed == b'6':
            self.raio = 80.0
        if self.key_pressed == b'7':
            self.raio = 90.0
        if self.key_pressed == b'8':
            self.raio = 100.0
        if self.key_pressed == b'9':
            self.raio = 110.0


        glutPostRedisplay()

if __name__ == "__main__":
    App()
