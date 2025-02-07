import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Function to generate 3D heart shape
def heart_shape():
    vertices = []
    for t in np.linspace(0, 2 * np.pi, 500):
        # Parametric equations for a heart shape in 3D
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        z = np.sin(t) * 0.5  # Add some 3D depth effect
        vertices.append((x, y, z))
    
    return vertices

# Initialize Pygame + OpenGL (Fullscreen)
pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN | DOUBLEBUF | OPENGL)  # Fullscreen mode
gluPerspective(45, (pygame.display.Info().current_w / pygame.display.Info().current_h), 0.1, 50.0)
glTranslatef(0.0, 0.0, -25)  # Move the shape further away to be visible

heart_vertices = heart_shape()

# Variables for rotation control
rotation_x = 0
rotation_y = 0

running = True
angle = 0

while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:  # Rotate left (around Y-axis)
                rotation_y -= 5
            if event.key == K_RIGHT:  # Rotate right (around Y-axis)
                rotation_y += 5
            if event.key == K_UP:  # Rotate up (around X-axis)
                rotation_x -= 5
            if event.key == K_DOWN:  # Rotate down (around X-axis)
                rotation_x += 5

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    glRotatef(rotation_x, 1, 0, 0)  # Rotate around X-axis
    glRotatef(rotation_y, 0, 1, 0)  # Rotate around Y-axis
    
    glPointSize(5)  # Increase particle size for visibility
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)  # Red color for heart
    for v in heart_vertices:
        glVertex3fv(v)
    glEnd()
    
    glPopMatrix()
    
    pygame.display.flip()

pygame.quit()
