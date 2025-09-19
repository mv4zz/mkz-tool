import cv2
import numpy as np
import winsound
import time

# Settings
URL = "http://192.168.0.20:8080/videofeed"
SCALE_FACTOR = 0.5
CONNECTION_TIMEOUT = 5  # seconds

# Connection monitoring variables
last_success_time = time.time()
connection_quality = "Excellent"
frame_count = 0
fps = 0
cap = cv2.VideoCapture(URL)

def play_connection_sound(status):
    try:
        if status == "connected":
            winsound.Beep(1000, 200)
        elif status == "poor":
            winsound.Beep(500, 400)
        elif status == "disconnected":
            winsound.Beep(200, 800)
    except:
        pass  # Skip audio if not available

while True:
    ret, frame = cap.read()
    current_time = time.time()
    
    try:
        if ret:
            last_success_time = current_time
            frame_count += 1
            
            # Calculate FPS safely
            if frame_count % 30 == 0:
                elapsed = max(0.001, current_time - last_success_time)  # Prevent division by zero
                fps = 30 / elapsed
                
                if fps > 20:
                    connection_quality = "Excellent"
                elif fps > 10:
                    connection_quality = "Good"
                    play_connection_sound("poor")
                else:
                    connection_quality = "Poor"
                    play_connection_sound("poor")
            
            # Process frame
            small_frame = cv2.resize(frame, (0,0), fx=SCALE_FACTOR, fy=SCALE_FACTOR)
            h, w = small_frame.shape[:2]
            
            # Visual connection status indicator
            status_color = (0, 255, 0) if connection_quality == "Excellent" else \
                         (0, 255, 255) if connection_quality == "Good" else \
                         (0, 0, 255)
            
            # Draw status elements
            cv2.circle(small_frame, (w-20, 20), 8, status_color, -1)
            cv2.putText(small_frame, f"Status: {connection_quality} ({int(fps)} FPS)", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, status_color, 2)
            
            cv2.imshow('Phone Cam - Connection Monitor', small_frame)
        else:
            # Disconnected state
            if current_time - last_success_time > CONNECTION_TIMEOUT:
                play_connection_sound("disconnected")
                blank = np.zeros((480, 640, 3), dtype=np.uint8)
                cv2.putText(blank, "CONNECTION LOST - Press Q to quit", (50, 200),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                cv2.imshow('Phone Cam - Connection Monitor', blank)
                
    except Exception as e:
        print(f"Error: {e}")  # Print error without crashing
        time.sleep(0.1)  # Small delay to prevent busy loop
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()