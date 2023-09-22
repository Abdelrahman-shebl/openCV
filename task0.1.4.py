import cv2 as cv
import os 

if not os.path.exists("Recordings"):
    os.makedirs("Recordings")

frames_per_seconds =24.0

video=cv.VideoCapture(0)
width=int(video.get(3))
height=int(video.get(4))
fourcc = cv.VideoWriter_fourcc(*'XVID')
cv.namedWindow("window")

recording = False

while video.isOpened():
    ret , frame =video.read()
    cv.imshow("window",frame)
    key=cv.waitKey(1)
    if key == ord('r'):
        recording = True
        if recording:
            filename = "Recordings/video_{}.avi".format(len(os.listdir("Recordings")))
            out = cv.VideoWriter(filename, fourcc, frames_per_seconds, (width, height))

            print("Recording started.")
    if key == ord('p'):
        recording = False
        print("Recording paused.")
    if key == ord('c'):
        recording = True
        print("Recording continued.")
    if key == ord('s'):
        recording = False
        out.release()
        print("Recording stoped.")

    if recording:
        out.write(frame)

    if cv.waitKey(1) == 27:
        break
    
video.release()
            