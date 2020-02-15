import cv2
import pygame

FILTER_DIR = "data/filters/"


class Draw:
    def draw_boundaries(self, frame, color):
        face = self.__dict__
        for face_part in face.keys():
            if not isinstance(face[face_part], float):
                x, y, w, h = face[face_part].boundaries
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    def draw_landmarks(self, frame, color):
        face = self.__dict__
        for face_part in face.keys():
            if not isinstance(face[face_part], float):
                for (x, y) in face[face_part].coordinates:
                    cv2.circle(frame, (x, y), 2, color)

    def draw_filter(self, screen, filter_name, face_part, which_part="all"):
        face = self.__dict__

        if which_part is "left":
            x, y, w, h = face[face_part].boundaries_left
        elif which_part is "right":
            x, y, w, h = face[face_part].boundaries_right
        else:
            x, y, w, h = face[face_part].boundaries

        image = pygame.image.load(FILTER_DIR + filter_name + ".png")
        image = pygame.transform.scale(image, (w, h))
        image = pygame.transform.rotate(image, self.rotation)
        screen.blit(image, (640 - x - w, y))

