####### START #######
# create and run a pygame display
# init
#

import pygame  # 1

import effects  # 12

from sys import exit  # 9

# init all of the pygame modules
# pygame.init()  # 2 (numpass, numfail)
pygame.display.init()  # 2

# pygame can only have one display active at a time
display: pygame.Surface = pygame.display.set_mode(  # 3
    size=(640, 480),
    flags=pygame.SCALED,  # change something about the display
    depth=0,  # number of bits to use for color
    display=0,  # which monitor to display the pygame window on
    vsync=1,  # request that the display vet
)

# 18
clock = pygame.time.Clock()

# by only allowing the events we need to use
# we can optimize our event queue
pygame.event.set_allowed(
    [pygame.QUIT, pygame.MOUSEBUTTONDOWN]
)  # 11 -next-> Particle.py

# list used to hold particles that should be drawn and updated
live_particles: list = []  # 13

while 1:  # 4
    clock.tick(60) # 19
    # clear display by filling
    display.fill((10, 10, 10, 255))  # 5

    # check event type to determine the input type
    # knowing the type also tells us what attributes
    # the event object will have
    for event in pygame.event.get():  # 7
        if event.type == pygame.QUIT:  # 8
            exit()  # 10

        elif event.type == pygame.MOUSEBUTTONDOWN:  # 14
            if event.button == 1:  # 15 (left click)

                live_particles.extend(
                    effects.get_explosion_particles(start_position=event.pos)
                )  # 16

    # 17
    ####### update and draw #######
    if 0 < len(live_particles):  # if there are active particles
        # particle loop
        for particle in live_particles:
            particle.update()

            if particle.alpha == 0:
                live_particles.remove(particle)
            else:
                pygame.draw.circle(
                    surface=display,
                    color=particle.color,
                    center=particle.center,
                    radius=particle.radius,
                )

    # updates pygame display
    # will not work for OPENGL displays
    # pass a rect (x, y, width, height) or a list of rects
    # if you want to only update a portion of the screen
    pygame.display.update()  # 6

    # updates entire display
    # pygame.display.flip()
