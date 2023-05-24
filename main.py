import pygame
from pygame.locals import *
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


ground_vertices = (
    (-100, -12.1, 200),
    (100, -12.1, 200),
    (-100, -12.1, -1000),
    (100, -12.1, -1000)
)


def render_text(text, x, y, z, size=1):
    font = pygame.font.Font(None, int(36 * size))
    text_surface = font.render(text, True, (255, 255, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width = text_surface.get_width()
    height = text_surface.get_height()

    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(size, size, size)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-width / 2, -height / 2, 0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(width / 2, -height / 2, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(width / 2, height / 2, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-width / 2, height / 2, 0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glDisable(GL_BLEND)
    glPopMatrix()


def draw_ground():
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0.0, 0.5, 0.5))
        glVertex3fv(vertex)
    glEnd()


def draw_restaurant():
    """Draw a 3D room with walls, ceiling, and floor"""

    # Set the color of the walls
    wall_color = (0.8, 0.8, 0.8)

    # Draw the walls
    glBegin(GL_QUADS)
    glColor3f(*wall_color)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)

    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glEnd()

    # Set the color of the ceiling and floor
    ceiling_color = (0.5, 0.5, 0.5)
    floor_color = (0.3, 0.3, 0.3)

    # Draw the ceiling and floor
    glBegin(GL_QUADS)
    glColor3f(*ceiling_color)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    glColor3f(*floor_color)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glEnd()

    glPushMatrix()
    glTranslatef(-.25, -1.0, 0)
    glScalef(0.3, 0.3, 0.3)
    draw_table()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(.55, -0.85, 0)
    glScalef(0.3, 0.3, 0.3)
    draw_chair()
    glPopMatrix()

    render_text("Prajjwal", 0, 0, -500, 40)


def draw_table():
    glBegin(GL_QUADS)
    # Table top
    glColor3f(1.0, 0.0, 0.5)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    # Table legs
    glColor3f(0.0, 1.0, 0.8)
    glVertex3f(-0.8, 0, -0.8)
    glVertex3f(-0.6, 0, -0.8)
    glVertex3f(-0.6, 1, -0.8)
    glVertex3f(-0.8, 1, -0.8)
    glVertex3f(-0.8, 0, -0.6)
    glVertex3f(-0.6, 0, -0.6)
    glVertex3f(-0.6, 1, -0.6)
    glVertex3f(-0.8, 1, -0.6)
    glVertex3f(-0.8, 0, 0.6)
    glVertex3f(-0.6, 0, 0.6)
    glVertex3f(-0.6, 1, 0.6)
    glVertex3f(-0.8, 1, 0.6)
    glVertex3f(-0.8, 0, 0.8)
    glVertex3f(-0.6, 0, 0.8)
    glVertex3f(-0.6, 1, 0.8)
    glVertex3f(-0.8, 1, 0.8)
    glVertex3f(0.6, 0, -0.8)
    glVertex3f(0.8, 0, -0.8)
    glVertex3f(0.8, 1, -0.8)
    glVertex3f(0.6, 1, -0.8)
    glVertex3f(0.6, 0, -0.6)
    glVertex3f(0.8, 0, -0.6)
    glVertex3f(0.8, 1, -0.6)
    glVertex3f(0.6, 1, -0.6)
    glVertex3f(0.6, 0, 0.6)
    glVertex3f(0.8, 0, 0.6)
    glVertex3f(0.8, 1, 0.6)
    glVertex3f(0.6, 1, 0.6)
    glVertex3f(0.6, 0, 0.8)
    glVertex3f(0.8, 0, 0.8)
    glVertex3f(0.8, 1, 0.8)
    glVertex3f(0.6, 1, 0.8)
    glEnd()


def draw_chair():
    # Draw the seat
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(-0.5, -0.1, -0.5)
    glVertex3f(0.5, -0.1, -0.5)
    glVertex3f(0.5, -0.1, 0.5)
    glVertex3f(-0.5, -0.1, 0.5)
    glEnd()

    # Draw the backrest
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-0.5, 0.5, -0.1)
    glVertex3f(0.5, 0.5, -0.1)
    glVertex3f(0.5, -0.1, -0.1)
    glVertex3f(-0.5, -0.1, -0.1)
    glEnd()

    # Draw the front legs
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-0.4, -0.1, 0.4)
    glVertex3f(-0.3, -0.1, 0.4)
    glVertex3f(-0.3, -0.5, 0.4)
    glVertex3f(-0.4, -0.5, 0.4)

    glVertex3f(0.4, -0.1, 0.4)
    glVertex3f(0.3, -0.1, 0.4)
    glVertex3f(0.3, -0.5, 0.4)
    glVertex3f(0.4, -0.5, 0.4)
    glEnd()

    # Draw the back legs
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glVertex3f(-0.4, -0.1, -0.4)
    glVertex3f(-0.3, -0.1, -0.4)
    glVertex3f(-0.3, -0.5, -0.4)
    glVertex3f(-0.4, -0.5, -0.4)

    glVertex3f(0.4, -0.1, -0.4)
    glVertex3f(0.3, -0.1, -0.4)
    glVertex3f(0.3, -0.5, -0.4)
    glVertex3f(0.4, -0.5, -0.4)
    glEnd()


def draw_shops():
    glPushMatrix()
    glScalef(10, 15, 10)
    glTranslatef(2, 0, 5)
    draw_restaurant()
    glPopMatrix()

    glPushMatrix()
    glScalef(3, 4, 3)
    glTranslatef(-15, 0, 0)
    glRotatef(90, 0, 0, 1)
    draw_shop()
    glPopMatrix()

    glPushMatrix()
    glScalef(3, 4, 3)
    glTranslatef(-8, 0, 10)
    glRotatef(90, 0, 0, 1)
    draw_shop()
    glPopMatrix()

    glPushMatrix()
    glScalef(3, 4, 3)
    glTranslatef(14, 0, 10)
    glRotatef(90, 0, 0, 1)
    draw_shop()
    glPopMatrix()

    glPushMatrix()
    glScalef(3, 4, 3)
    glTranslatef(-15, 0, 20)
    glRotatef(90, 0, 0, 1)
    draw_shop()
    glPopMatrix()

    glPushMatrix()
    glScalef(10, 15, 10)
    glTranslatef(4, 0, 12)
    draw_restaurant()
    glPopMatrix()

    glPushMatrix()
    glScalef(10, 15, 10)
    glTranslatef(-4, 0, 15)
    draw_restaurant()
    glPopMatrix()


def draw_shop():
    # Walls
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_QUADS)
    glVertex3f(-5, -5, 0)
    glVertex3f(-5, 5, 0)
    glVertex3f(5, 5, 0)
    glVertex3f(5, -5, 0)
    glEnd()

    # Ceiling
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(-5, -5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, -5, 5)
    glEnd()

    # Floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-5, -5, 0)
    glVertex3f(-5, 5, 0)
    glVertex3f(5, 5, 0)
    glVertex3f(5, -5, 0)
    glEnd()

    # Shelves
    glColor3f(0.5, 0.5, 0.5)
    for i in range(-3, 4, 2):
        glBegin(GL_QUADS)
        glVertex3f(i - .15, -3, 2)
        glVertex3f(i - .15, 3, 2)
        glVertex3f(i + .15, 3, 2)
        glVertex3f(i + .15, -3, 2)
        glEnd()

    # Boxes
    glColor3f(78/255, 53/255, 36/255)
    glPushMatrix()
    glTranslatef(-2.5, -1, 1)
    glutSolidCube(1)
    glPopMatrix()
    glColor3f(78/255, 53/255, 36/255)
    glPushMatrix()
    glTranslatef(-2.5, 1, 1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.5, 0, 1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.7, 0, 1)
    glutSolidCube(1)
    glPopMatrix()


stars = []
for i in range(100):
    x = random.uniform(-50, 50)
    y = random.uniform(-50, 50)
    z = random.uniform(-50, 50)
    size = random.uniform(0.1, 0.5)
    brightness = random.uniform(0.1, 0.5)
    stars.append((x, y, z, size, brightness))


def draw_star(x, y, z, size, brightness):
    glColor4f(brightness, brightness, brightness, brightness)
    glBegin(GL_QUADS)
    glVertex3f(x - size, y - size, z)
    glVertex3f(x + size, y - size, z)
    glVertex3f(x + size, y + size, z)
    glVertex3f(x - size, y + size, z)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)

    glTranslatef(0.0, -0.0, -200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                elif event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                elif event.key == pygame.K_UP:
                    glTranslatef(0, 0, 0.5)
                elif event.key == pygame.K_DOWN:
                    glTranslatef(0, 0, -0.5)
        glutInit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.set_caption("3D Shopping Mall")

        # draw the stars
        for star in stars:
            draw_star(*star)

        glPushMatrix()
        glScalef(3, 4, 3)
        glTranslatef(-10, 0, 0)
        draw_ground()
        glPopMatrix()
        draw_shops()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
