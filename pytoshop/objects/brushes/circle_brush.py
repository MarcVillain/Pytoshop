from pytoshop.objects.brush_o import Brush

from math import sqrt


class CircleBrush(Brush):

    def __init__(self):
        super().__init__()

    def draw(self, layer, point):
        x0, y0 = point

        color = self.color
        radius = self.size // 2
        hardness = self.hardness / 100
        opacity = self.opacity / 100

        # Drawing middle lines
        for i, j in [0, 1], [1, 0]:
            for delta in range(-radius, radius + 1):
                x, y = x0 + delta*i, y0 + delta*j

                d = ((x0 - x) ** 2 + (y0 - y) ** 2) / (radius * radius)
                if d <= 1:
                    a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)  # exp(-7*d)
                    a *= opacity
                    if layer.canDrawAt(x, y):
                        layer.draw(x, y, color, a)

        # Drawing outer circle
        for dy in range(1, radius + 1):
            for dx in range(1, radius + 1):
                xA, yA = x0 + dx, y0 + dy
                xB, yB = x0 - dx, y0 + dy
                xC, yC = x0 + dx, y0 - dy
                xD, yD = x0 - dx, y0 - dy

                d = ((x0 - xA) ** 2 + (y0 - yA) ** 2) / (radius*radius)
                if d <= 1:
                    a = 1 if d < hardness or hardness == 1 else (1 - d) / (1 - hardness)  # exp(-7*d)
                    a *= opacity
                    if layer.canDrawAt(xA, yA):
                        layer.draw(xA, yA, color, a)
                    if layer.canDrawAt(xB, yB):
                        layer.draw(xB, yB, color, a)
                    if layer.canDrawAt(xC, yC):
                        layer.draw(xC, yC, color, a)
                    if layer.canDrawAt(xD, yD):
                        layer.draw(xD, yD, color, a)