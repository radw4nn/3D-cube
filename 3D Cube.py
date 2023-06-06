import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up the OpenGL perspective
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)


# Set up the cube vertices
vertices = (
    (-1, -1, -1),
    (-1, 1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, 1),
    (1, -1, 1)
)

# Set up the cube edges
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

# Set the initial rotation values
x_rotation = 0
y_rotation = 0

# Render the rotating cube
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glRotatef(x_rotation, 1, 0, 0)
    glRotatef(y_rotation, 0, 1, 0)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

    # Update the rotation values
    x_rotation += 0.5
    y_rotation += 0.5
