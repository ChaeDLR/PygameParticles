from pygame import Vector2  # 8

from random import randint  # 5

from particle import Particle  # 1

# 1
def get_explosion_particles(start_position: tuple[int, int]) -> list[Particle]:
    """
    return a list of particles that have slopes
    that create and explosion effect
    """
    particles: list[Particle] = []  # 3

    ####### 4 #######
    # modifiers for a particles (x, y) movement
    # (-1) -> invert
    # 0 -> zero out increment. Do not move across the axis
    # 1 -> keep the default direction
    directions: tuple[tuple[int, int]] = (
        # left
        (-1, 0),
        # right
        (1, 0),
        # up
        (0, -1),
        # down
        (0, 1),
        # top left
        (-1, -1),
        # bottom left
        (-1, 1),
        # top right
        (1, -1),
        # bottom right
        (1, 1),
    )
    ####### 4 #######

    ####### 5 #######
    # Generate pseudorandom color tuples
    # all alpha values start at fully opaque (255)
    colors: list[list[int, int, int, int]] = [
        [randint(20, 230), randint(20, 230), randint(20, 230), 255] for _ in range(4)
    ]
    ####### 5 #######

    # 7
    velocity: int = 30

    ####### 8 #######
    # this loop creates a new particle layer
    # color, radius, rate of change
    for i, color in enumerate(colors):  # layer

        # add 1 to the index because a radius lower than 1 won't display
        radius: int = i + 1

        # get the percentage this particle's ROC should be
        # 100% = full speed
        # higher velocity and lower radius = faster particle movement and alpha ROC
        roc_percentage: float = (velocity / radius) / velocity

        # get a particle for each direction the effect needs
        # calculate slope and append a new Particle
        for direction in directions:  # particles

            # x & y values the particle will inc by
            slope: tuple = (
                (direction[0] * velocity) * roc_percentage,  # X
                (direction[1] * velocity) * roc_percentage,  # Y
            )

            particles.append(
                Particle(
                    color=color,
                    center=Vector2(start_position),
                    slope=slope,
                    radius=radius,
                )
            )

    return particles
    ####### 8 #######
    # -next-> main_loop.py
