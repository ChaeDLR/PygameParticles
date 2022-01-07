import pygame

import effects

from sys import exit

# init all of the pygame modules
# pygame.init() -> (numpass, numfail)
pygame.display.init()

# pygame can only have one display active at a time
display: pygame.Surface = pygame.display.set_mode(
    size=(640, 480),
    flags=pygame.SCALED,  # change something about the display
    depth=0,  # number of bits to use for color
    display=0,  # which monitor to display the pygame window on
    vsync=1,  # request that the display vet
)

clock = pygame.time.Clock()

# by only allowing the events we need to use
# we can optimize our event queue
pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])

# list used to hold particles that should be drawn and updated
live_particles: list = []

while 1:
    clock.tick(60)
    # clear display by filling
    display.fill((10, 10, 10, 255))

    # check event type to determine the input type
    # knowing the type also tells us what attributes
    # the event object will have
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                live_particles.extend(
                    effects.get_explosion_particles(start_position=event.pos)
                )

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
    pygame.display.update()

    # updates entire display
    # pygame.display.flip()
