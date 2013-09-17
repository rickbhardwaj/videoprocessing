#NOTES FOR SERGIO

#Use import cv for OpenCV 2.1-2.3 functionality, use import cv2 for OpenCV 2.4 < functionality

#PYTHONPATH in system variables is not reliable and stable, espicially across machines and OSes.
#Try to use full path names whenever possible, such as the haar cascade loading functions below

import cv

capture = cv.CaptureFromCAM(0)



imcolor = cv.QueryFrame(capture) # input image
cv.NamedWindow('Return Window', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Return Window', imcolor) 
# loading the classifiers
haarFace = cv.Load('C:/Users/Rick/Documents/OpenCV 2.1/OpenCV-2.1.0-win/OpenCV-2.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
haarEyes = cv.Load('C:/Users/Rick/Documents/OpenCV 2.1/OpenCV-2.1.0-win/OpenCV-2.1.0/data/haarcascades/haarcascade_eye.xml')
# running the classifiers
storage = cv.CreateMemStorage()
detectedFace = cv.HaarDetectObjects(imcolor, haarFace, storage)
detectedEyes = cv.HaarDetectObjects(imcolor, haarEyes, storage)

# draw a green rectangle where the face is detected
if detectedFace:
    for face in detectedFace:
        cv.Rectangle(imcolor,(face[0][0],face[0][1]),
               (face[0][0]+face[0][2],face[0][1]+face[0][3]),
               cv.RGB(155, 255, 25),2)

# draw a purple rectangle where the eye is detected
if detectedEyes:
    for face in detectedEyes:
        cv.Rectangle(imcolor,(face[0][0],face[0][1]),
               (face[0][0]+face[0][2],face[0][1]+face[0][3]),
               cv.RGB(155, 55, 200),2)

cv.NamedWindow('Face Detection', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Face Detection', imcolor) 
cv.WaitKey()
