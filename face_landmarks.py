import numpy as np
import face_draw


def calculate_boundaries(points):
    x = min(points[:, 0])
    y = min(points[:, 1])
    w = max(points[:, 0]) - x
    h = max(points[:, 1]) - y
    return x, y, w, h


def calculate_rotation(points):
    w = points[-1][0] - points[0][0]
    h = points[-1][1] - points[0][1]
    return np.math.atan(h / w) * 180 / np.pi


class FaceShape:
    def __init__(self, points):
        self.coordinates = points[0:17]
        self.boundaries = calculate_boundaries(self.coordinates)


class Eyebrows:
    def __init__(self, points):
        self.coordinates_left = points[17:22]
        self.coordinates_right = points[22:27]
        self.coordinates = points[17:27]
        self.boundaries_left = calculate_boundaries(self.coordinates_left)
        self.boundaries_right = calculate_boundaries(self.coordinates_right)
        self.boundaries = calculate_boundaries(self.coordinates)


class Nose:
    def __init__(self, points):
        self.coordinates = points[27:36]
        self.boundaries = calculate_boundaries(self.coordinates)


class Eyes:
    def __init__(self, points):
        self.coordinates_left = points[36:42]
        self.coordinates_right = points[42:48]
        self.coordinates = points[36:48]
        self.boundaries_left = calculate_boundaries(self.coordinates_left)
        self.boundaries_right = calculate_boundaries(self.coordinates_right)
        self.boundaries = calculate_boundaries(self.coordinates)


class Lips:
    def __init__(self, points):
        self.coordinates_external = points[48:60]
        self.coordinates_internal = points[60:68]
        self.coordinates = points[48:68]
        self.boundaries_external = calculate_boundaries(self.coordinates_external)
        self.boundaries_internal = calculate_boundaries(self.coordinates_internal)
        self.boundaries = calculate_boundaries(self.coordinates)


class Face(face_draw.Draw):
    def __init__(self, points):
        self.face_shape = FaceShape(points)
        self.eyebrows = Eyebrows(points)
        self.eyes = Eyes(points)
        self.nose = Nose(points)
        self.lips = Lips(points)

        self.rotation = calculate_rotation(self.face_shape.coordinates)

