import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the primary camera

# Define the setpoint
setpoint_x, setpoint_y = 320, 240  # Example coordinates

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        break

    # Calculate the camera's center bottom point
    height, width = frame.shape[:2]
    center_bottom_x = width // 2
    center_bottom_y = height - 30 # Bottom of the frame
    

    # Mark the setpoint in the frame
    cv2.circle(frame, (setpoint_x, setpoint_y), 5, (0, 255, 0), -1)  # Green dot

    # Mark the camera's center bottom point
    cv2.circle(frame, (center_bottom_x, center_bottom_y), 5, (0, 0, 255), -1)  # Red dot

    # Calculate the error
    error_x = setpoint_x - center_bottom_x
    error_y = setpoint_y - center_bottom_y

    #Display the error calculated 
    print(error_x)
    print(error_y)

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
