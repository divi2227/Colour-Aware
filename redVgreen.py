import numpy as np
import cv2
import pyttsx3

# Initialize webcam
webcam = cv2.VideoCapture(0)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Flags to prevent repeating voice every frame
spoken_veg = False
spoken_nonveg = False

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red and green color ranges (tuned for the symbol shades)
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    # Create masks
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    # Dilate to strengthen detection
    kernel = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(red_mask, kernel)
    green_mask = cv2.dilate(green_mask, kernel)

    # Detect red contours (non-veg)
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detected_nonveg = False
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "NON-VEG", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            detected_nonveg = True

    # Detect green contours (veg)
    contours_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detected_veg = False
    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "VEG", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            detected_veg = True

    # Speak based on detection
    if detected_veg and not spoken_veg:
        engine.say("Vegetarian")
        engine.runAndWait()
        spoken_veg = True
        spoken_nonveg = False
    elif detected_nonveg and not spoken_nonveg:
        engine.say("Non Vegetarian")
        engine.runAndWait()
        spoken_nonveg = True
        spoken_veg = False
    elif not detected_veg and not detected_nonveg:
        spoken_veg = False
        spoken_nonveg = False

    # Show output
    cv2.imshow("Veg/Non-Veg Symbol Detector", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
webcam.release()
cv2.destroyAllWindows()
