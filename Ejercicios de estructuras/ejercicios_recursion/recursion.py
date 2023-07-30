# Circle and rectangle overlapping
# example: https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png

"""You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned
rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner,
and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false.
In other words,
check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time."""

"""Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0)."""


def overlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return False
    closestX = min(max(xCenter, x1), x2)
    closestY = min(max(yCenter, y1), y2)
    distanceX = xCenter - closestX
    distanceY = yCenter - closestY
    distanceSquared = distanceX * distanceX + distanceY * distanceY
    return distanceSquared <= radius * radius or overlap(radius, xCenter, yCenter, x1 + 1, y1 + 1, x2 - 1, y2 - 1)


"""A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1 The area of the rectangular web page you designed must equal to the given target area.
2 The width W should not be larger than the length L, which means L >= W.
3 The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence."""


def construct_area(area: int, main_flag=False, flag=False, factores=None, contador=None) -> list[large:int, width: int]:
    # definir variables, se protegen de la recursividad por medio de flags
    if not flag:
        contador: int = 1
        factores: list = []
        flag = True

    # Hallar factores del area
    if not main_flag:
        if area % contador == 0 and contador < area:
            factores.append(contador)

        if contador == area:
            return construct_area(area, True, True, factores, contador)

        contador += 1

        return construct_area(area, False, True, factores, contador)


import copy

def hallar_convinatorias(factores: list, main_flag=False, flag=False, comparativas: list = None):
    if not flag:
        comparativas: list = []

    if not main_flag:
        copia = copy.deepcopy(factores)
        comparativas.append(copia * len(factores))

        return hallar_convinatorias(factores, True, True, comparativas)

    if comparativas[0] is not None:

