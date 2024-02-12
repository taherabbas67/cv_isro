import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the yellow objects detected
    cv2.imshow('Frame', frame)
    cv2.imshow('Yellow Objects Detected', res)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
