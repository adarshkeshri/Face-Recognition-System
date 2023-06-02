import cv2 as cv
import sys
def face_recog():
    people = []

    with open(r'C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/Dataset/name_list.txt', 'r') as fp:
        for line in fp:
            x = line[:-1]
            people.append(x)

    haar_cascade = cv.CascadeClassifier('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/MainCode/haar_face.xml')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/MainCode/face_trainer.yml')

    video_capture = cv.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)

        face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 4)
        for (x,y,w,h) in face_rect:
            faces_roi = gray[y:y+h, x: x+h]

            label,confidence = face_recognizer.predict(faces_roi)
            if confidence<50:
                print("Unknown Face")
                cv.putText(frames,"Unknown Face", (20,20), cv.FONT_HERSHEY_COMPLEX,1.0, (0,0,255), thickness = 2)
                cv.rectangle(frames, (x,y), (x+w,y+h), (0,0,255), thickness = 1)
            else:  
                print(f'Label = {people[label]} with a confidence of {confidence}')
                cv.putText(frames, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), thickness = 2)
                cv.rectangle(frames, (x,y), (x+w,y+h), (0,255,0), thickness = 1)
                
        # Display the resulting frame
        cv.imshow('Attendance', frames)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break