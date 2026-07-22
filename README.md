# AI Face Detection

## Overview

This project is an AI-powered face detection program built with Python and OpenCV. It uses a Haar Cascade Classifier to detect human faces in real time through a webcam. When a face is detected, the program draws a rectangle around it using a randomly generated color.

## Features

* Detects faces in real time using a webcam.
* Draws colorful rectangles around detected faces.
* Uses OpenCV's Haar Cascade face detection model.
* Press **Q** to close the program.

## Technologies Used

* Python 3
* OpenCV (`cv2`)
* Haar Cascade Classifier
* Random module

## Requirements

Before running the project, install the required library:

```bash
pip install opencv-python
```

You also need the following file in the same folder as your Python program:

* `haarcascade_frontalface_default.xml`

This file comes with OpenCV and can also be downloaded from the official OpenCV GitHub repository.

## How It Works

1. Opens your computer's webcam.
2. Captures each video frame.
3. Converts the frame to grayscale.
4. Detects faces using the Haar Cascade Classifier.
5. Draws a colored rectangle around each detected face.
6. Displays the live webcam feed with face detection.

## How to Run

1. Download or clone this repository.
2. Make sure `haarcascade_frontalface_default.xml` is in the project folder.
3. Install OpenCV if you haven't already.
4. Run the program:

```bash
python face_detection.py
```

5. Press **Q** to exit the application.

## Author

**Sufia Khan**

## License

This project is for educational purposes.
