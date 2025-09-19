import cv2

# Open the webcam feed (e.g., from index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam. Check if the camera is connected and not in use by another application.")
    exit()

print("Webcam is open. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Display the resulting frame
    cv2.imshow("Webcam Feed", frame)

    # Wait for 1 ms and check if 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("'q' pressed. Exiting...")
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()