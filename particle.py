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
        self.__alpha_inc: float = 20 / self.radius  # 8

    ####### 9 #######
    @property
    def alpha(self):
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
    def update(self):
        """update the particles values"""
        self.center.x += self.slope[0]
        self.center.y += self.slope[1]

        self.alpha -= self.__alpha_inc
        ####### 10 #######


# -next-> effects.py

# TODO: Update non-particle dataclass if this new layout works

# class Particle:  # 12
#     """particle model"""

#     def __init__(  # 13
#         self,
#         color: list[int, int, int, int],
#         center: list[int, int],
#         slope: tuple[int, int],
#         radius: float,
#     ):
#         """initialize everything needed to draw and update"""
#         ####### 14 #######
#         self.color: list[int, int, int, int] = color
#         self.center: list[int, int] = center
#         self.slope: tuple[int, int] = slope
#         self.radius: float = radius
#         ####### 14 #######

#         ####### 15 #######
#         self.__alpha: float = 255.0
#         self.__alpha_inc: float = 20 / self.radius
#         ####### 15 #######
