import cv2

face_cap = cv2.CascadeClassifier("C:/Program Files/Python311/Lib/site-packages/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml")
videoCap = cv2.VideoCapture(0)

while True:
    ret, video = videoCap.read()
    col = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("video.live", video)
    
    if cv2.waitKey(10) == ord("a"):
        break

videoCap.release()
cv2.destroyAllWindows()
