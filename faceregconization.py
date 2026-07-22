#OpenCV libary for image processing
import cv2
#randrange function to generate random numbers for retangle colors
from random import randrange
#in the modelcode.xml, haarcascade contains data used to detect faces
brain=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

#start VideoCapture using the defult webcam
camera=cv2.VideoCapture(0)
while True:
    #read single frame from the webcam 
    success, frame = camera.read()
    #converts the captured frame to grey scale(becayse face detection works better on gray scale image)    
    greyscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #it returns list of retangles with(x,y,width,height) for each detected face(face coordinates)
    facesqaure=brain.detectMultiScale(greyscale)
    #draw retangles around each detected phase.
    for (x,y,w,h) in facesqaure:
        #use random colors and thickness of 2 for the retangle 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)
    print(facesqaure)
   #show the frame with triangles in window title "Face Detector" 
    cv2.imshow("Face Detector",frame)
    #wait one millisecond for key press
    key=cv2.waitKey(1)
    if key==81 or key==113:
        camera.release()
        cv2.destroyAllWindows()
        break
