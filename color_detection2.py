import cv2
import numpy as np

# Function to find center coordinates of contours
def find_contour_center(contour):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return cX, cY
    else:
        return None, None

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize variables to keep track of best yellow contour and its mean brightness
best_yellow_contour = None
best_brightness = -1

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

    # Find contours of yellow objects
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for contour in contours:
        # Calculate the mean brightness of the contour
        brightness = cv2.mean(hsv_frame, mask=mask)[2]

        # Update best contour if current contour is brighter
        if brightness > best_brightness:
            best_brightness = brightness
            best_yellow_contour = contour

    # If best contour is found, find and print its center coordinates
    if best_yellow_contour is not None:
        center_x, center_y = find_contour_center(best_yellow_contour)
        if center_x is not None and center_y is not None:
            # Draw a circle at the center
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
            # Print the coordinates
            print("Center coordinates of best yellow contour: ({}, {})".format(center_x, center_y))

    # Display the original frame with center points
    cv2.imshow('Frame', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
