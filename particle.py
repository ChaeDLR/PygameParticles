# create a class to model a particle
# with an update method
from dataclasses import dataclass  # python 3.7

from pygame import Vector2


@dataclass  # 2
class Particle:  # 1
    """dataclass to model a particle"""

    # particle color (red, green, blue, alpha)
    color: list[int, int, int, int]  # 3

    # starting point
    center: Vector2  # 4

    # steer the particle (x, y)
    slope: tuple[int, int]  # 5

    # distance from the center of the circle to the edge
    # any value lower than 1 will not display
    radius: float  # 6

    def __post_init__(self):  # 7
        """use the data we got to set movement and alpha rates of change"""
        # a private float variable to manage the value of color[3]
        # the lower this number is, the longer it takes to dissipate
        # used to reduce the particles alpha every call od the update method
        self.__dissipation_rate: float = 5 / self.radius  # 8

    ####### 9 #######
    @property
    def alpha(self) -> int:
        return self.color[3]

    @alpha.setter
    def alpha(self, value: float) -> None:
        if value < 20:
            self.color[3] = 0

        elif value > 255:
            self.color[3] = 255

        else:
            self.color[3] = value

    ####### 9 #######

    ####### 10 #######
    def update(self) -> None:
        """update the particles values"""
        self.center.x += self.slope[0]
        self.center.y += self.slope[1]

        self.alpha -= self.__dissipation_rate
    ####### 10 #######  -next-> effects.py



# class Particle:
#     """particle model"""

#     def __init__(
#         self,
#         color: list[int, int, int, int],
#         center: list[int, int],
#         slope: tuple[int, int],
#         radius: float,
#     ):
#         """initialize everything needed to draw and update"""

#         self.color: list[int, int, int, int] = color
#         self.center: list[int, int] = center
#         self.slope: tuple[int, int] = slope
#         self.radius: float = radius

#         self.__alpha_inc: float = 10 / self.radius
