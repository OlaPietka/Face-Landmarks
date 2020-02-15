import sys
import cv2
import numpy as np
import dlib
import pygame
from imutils import face_utils
import face_landmarks


if __name__ == "__main__":
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")

    #  Init display
    pygame.init()
    pygame.display.set_caption("Snapchat filters")
    screen = pygame.display.set_mode([640, 480])

    #  Sets the video source to the default webcam
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            face = face_landmarks.Face(landmarks)

            #  Mange screen
            frame = np.rot90(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0, 0))

            face.draw_filter(screen, "pinklips", face_part="lips")

        #  Display the resulting frame
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                sys.exit(0)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    pygame.quit()
