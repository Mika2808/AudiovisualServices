import cv2
import numpy as np
#------------------------------ 1 ---------------------------------

# Load input video
cap = cv2.VideoCapture("Videos/Individual/short.mov")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define video writers with two codecs
out1 = cv2.VideoWriter("output_mjpeg.avi", cv2.VideoWriter_fourcc(*'MJPG'), fps, (width, height), isColor=False)
out2 = cv2.VideoWriter("output_xvid.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height), isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Split top and bottom halves
    top_half = gray[:height//2, :]
    bottom_half = gray[height//2:, :]
    bottom_half_flipped = cv2.flip(bottom_half, 0)  # Flip vertically

    # Recombine
    combined = cv2.vconcat([top_half, bottom_half_flipped])

    out1.write(combined)
    out2.write(combined)

cap.release()
out1.release()
out2.release()


#------------------------------ 2 ---------------------------------
# Load video
cap = cv2.VideoCapture("Videos/Individual/short.mov")

# Output video writer
out = cv2.VideoWriter("color_quadrants.avi",
                      cv2.VideoWriter_fourcc(*'XVID'),
                      30, (1920, 1080))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to quarter (960x540)
    frame_small = cv2.resize(frame, (960, 540))

    # Create red, green, blue versions
    red_frame = frame_small.copy()
    red_frame[:, :, 0] = 0  # zero blue
    red_frame[:, :, 1] = 0  # zero green

    green_frame = frame_small.copy()
    green_frame[:, :, 0] = 0  # zero blue
    green_frame[:, :, 2] = 0  # zero red

    blue_frame = frame_small.copy()
    blue_frame[:, :, 1] = 0  # zero green
    blue_frame[:, :, 2] = 0  # zero red

    # Top row: normal + red
    top = np.concatenate((frame_small, red_frame), axis=1)

    # Bottom row: green + blue
    bottom = np.concatenate((green_frame, blue_frame), axis=1)

    # Final 1920x1080 frame
    final_frame = np.concatenate((top, bottom), axis=0)

    out.write(final_frame)

cap.release()
out.release()


#------------------------------ 3---------------------------------

# Load video
cap = cv2.VideoCapture("Videos/Individual/short.mov")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    cv2.imshow('Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


