import cv2
import pickle
import os
import numpy as np

# Initialize video and face detection
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Capture faces
faces_data = []
i = 0
name = input("Enter the name: ")
while True: 
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y: y+h, x: x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))  # Ensure consistent dimensions
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i += 1
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break

video.release()
cv2.destroyAllWindows()

# Prepare faces data
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)  # Ensure consistent reshaping

# Save or update names.pkl
try:
    if 'names.pkl' not in os.listdir('data/'):
        names = [name] * 100
    else:
        with open('data/names.pkl', 'rb') as f:
            names = pickle.load(f)
        names += [name] * 100
except (FileNotFoundError, pickle.UnpicklingError):
    print("Error loading names.pkl. Creating a new file.")
    names = [name] * 100

with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)

# Save or update faces_data.pkl
try:
    if 'faces_data.pkl' not in os.listdir('data/'):
        faces = faces_data
    else:
        with open('data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
        # Debugging: Print shapes before appending
        print(f"Existing faces shape: {faces.shape}")
        print(f"New faces_data shape: {faces_data.shape}")
        # Ensure shapes match before appending
        if faces.shape[1] == faces_data.shape[1]:
            faces = np.append(faces, faces_data, axis=0)
        else:
            print("Error: Mismatched shapes for faces and faces_data. Skipping append.")
except (FileNotFoundError, pickle.UnpicklingError):
    print("Error loading faces_data.pkl. Creating a new file.")
    faces = faces_data

with open('data/faces_data.pkl', 'wb') as f:
    pickle.dump(faces, f)

print("Data saved successfully!")