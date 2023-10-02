from OpenGL.GL import *
from OpenGL.GLUT import *

class App:
    def __init__(self):
        self.mouseX = 0.0
        self.mouseY = 0.0
        self.init_window()

    def normalize_x(self, x):
        return((x / 200.0) - 1.0)
    
    def normalize_y(self, y):
        return(-(y / 200.0) + 1.0)
    
    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(400, 400)
        glutCreateWindow(b"Desenhar Ponto no Clique do Mouse")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse_click)
        glutMainLoop()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        self.point()
        glFlush()

    def point(self):
        glBegin(GL_POINTS)  # Use GL_POINTS para desenhar pontos
        glVertex2d(self.normalize_x(self.mouseX), self.normalize_y(self.mouseY))
        glEnd()

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.mouseX = x
            self.mouseY = y
            glutPostRedisplay()  

if __name__ == "__main__":
    App()
