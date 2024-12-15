## Title of the Project
A Smart Attendance System using facial recognition technology to automatically mark attendance based on student faces, streamlining the attendance process and enhancing accuracy in educational institutions.

## About
The Smart Attendance System project integrates facial recognition technology to automate the process of marking student attendance in classrooms. The system captures images of students' faces and stores them for future recognition. Using a webcam, the system detects faces in real-time and matches them against the stored dataset to mark attendance.

Key Features:
Face Enrollment:

Students capture their face images via webcam and register their name.
100 images per student are captured for improved recognition accuracy.
Stored in a pickle file for fast retrieval.
Automated Attendance:

Uses K-Nearest Neighbors (KNN) to match detected faces with the stored dataset.
Marks attendance and saves the student's name with the timestamp to a CSV file.
Prevents duplicate attendance marking by tracking attended students.
Real-time Feedback:

Displays student names on the webcam feed when attendance is taken.
Provides audio feedback confirming successful attendance using Windows Speech API.
Streamlined Interface:

User-friendly interface built with Streamlit.
Easy navigation between "Add Faces" and "Take Attendance" options.
Accuracy and Efficiency:

High recognition accuracy using KNN classifier.
Real-time processing for quick attendance marking with minimal delay.
Goal:

Automates attendance marking, offering a more efficient, accurate, and scalable solution for educational institutions.
## Features
Features of the Smart Attendance System:
Face Enrollment: Allows students to register by capturing their face images through a webcam.
Real-Time Face Detection: Detects faces from webcam feed using Haar Cascade Classifier.
KNN-based Recognition: Uses K-Nearest Neighbors (KNN) classifier to recognize faces and mark attendance.
Automated Attendance Logging: Marks attendance when a student’s face is recognized and saves it in a CSV file.
Audio Feedback: Provides real-time audio feedback to confirm attendance marking using Windows Speech API.
Student Data Management: Stores and retrieves student face data and names using Pickle files.
Attendance History: Saves attendance records with timestamps in CSV files for each session.
User Interface: Streamlit-based interface for easy interaction and navigation between adding faces and taking attendance.
Duplicate Detection: Ensures each student’s attendance is recorded only once during a session.
Real-Time Visual Feedback: Displays student names on the video stream when their attendance is taken.


## Requirements
Project Requirements:
Software Requirements:

Python (3.x)
Streamlit
OpenCV
Scikit-learn
Numpy
Pickle
Windows Speech API (SAPI)
Hardware Requirements:

Webcam for capturing student faces
A computer with sufficient processing power for real-time face detection
External Libraries:

opencv-python for face detection and image processing
scikit-learn for KNN classification
numpy for numerical operations
pickle for storing and loading data
streamlit for creating the user interface
Dataset Requirements:

A collection of student face images (at least 100 per student for accurate recognition)
A CSV file to store attendance data
Miscellaneous:

Haar Cascade Classifier XML file for face detection (haarcascade_frontalface_default.xml)
A directory to save attendance logs (CSV files)

## System Architecture
<!--Embed the system architecture diagram as shown below-->
![image](https://github.com/user-attachments/assets/da9d502a-5ce9-4f99-b0ce-4088b43a764e)


## Output

<!--Embed the Output picture at respective places as shown below as shown below-->
#### Output1 - Interface
![image](https://github.com/user-attachments/assets/86acdf2d-80b6-4091-9185-1aee5c216411)


#### Output2 - Face captured
![Screenshot 2024-12-15 190320](https://github.com/user-attachments/assets/859d9541-7d84-4dd6-bcb6-749f69d6763c)


#### Output3 - Accuracy
![image](https://github.com/user-attachments/assets/35d22f39-fa9f-43b4-a9b7-40321eba3f58)

Detection Accuracy: 96.0%
Note: These metrics can be customized based on your actual performance evaluations.


## Results and Impact
<!--Give the results and impact as shown below-->
Automated Attendance: Reduces time and effort by eliminating manual attendance-taking.

High Accuracy: Ensures accurate attendance marking with face recognition and KNN classification.

Real-Time Feedback: Provides immediate visual and audio confirmation when attendance is marked.

Scalability: Can be easily adapted to handle larger databases and used in bigger institutions.

Improved User Experience: Streamlined, user-friendly interface for easy interaction.

Reduced Fraud: Minimizes proxy attendance by using face recognition technology.

Impact on Education: Helps educators focus more on teaching by automating attendance and providing accurate records.

This project serves as a foundation for future developments in assistive technologies and contributes to creating a more inclusive and accessible digital environment.

## Articles published / References
1. Chunduru Anilkumar; B Venkatesh; S Annapoorna, “Smart Attendance System with Face Recognition using OpenCV”, 22 September 2023
2. Jayaraj Viswanathan1, Kuralamudhan , Navaneethan and Veluchamy , “Smart Attendance System using Face Recognition”, Data Science Insights,  26 February 2024




