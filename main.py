import cv2
import numpy as np
from pynput.keyboard import Controller

keyboard = Controller()

cap = cv2.VideoCapture(0)

bg_subtractor = cv2.createBackgroundSubtractorMOG2()

prev_x, prev_y = None, None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask = bg_subtractor.apply(frame)
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust this threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if prev_x is not None and prev_y is not None:
                dx = x - prev_x
                dy = y - prev_y

                if dx > 20:  # Moving right
                    keyboard.press('d')
                    keyboard.release('d')
                elif dx < -20:  # Moving left
                    keyboard.press('a')
                    keyboard.release('a')
                if dy > 20:  # Moving down
                    keyboard.press('s')
                    keyboard.release('s')
                elif dy < -20:  # Moving up
                    keyboard.press('w')
                    keyboard.release('w')

            # Update previous positions
            prev_x, prev_y = x, y

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

