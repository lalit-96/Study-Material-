import cv2,time

video =cv2.VideoCapture(0)
frame_count=0
while True:
    frame_count=frame_count+1
    check,frame =video.read()
    print(check)
    print(frame)
    #time.sleep(3)


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",frame)
    cv2.waitKey(1000)
    if key==ord('q'):
        break
print(frame_count)
video.release()
cv2.destroyAllWindows()
