import cv2
from voice_rec import voice_rec
import time

face_cascade = cv2.CascadeClassifier('./haarcascade_upperbody.xml')
cap = cv2.VideoCapture(0)

def main():
    i=0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        #print(len(faces))
        
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = img[y: y + h, x: x + w]
            face_gray = gray[y: y + h, x: x + w]
            cv2.putText(img, 'Human Detected', (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,200), 2, cv2.LINE_AA)
            i+=1
        cv2.imshow('video image', img)
        
        
        if i>3:
            #cv2.imshow('video image', img)
            #time.sleep(2)
            
            voice_rec()
            i=0
            #break




        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

main()