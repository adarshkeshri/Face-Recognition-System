import cv2 as cv
import os
import numpy as np

def train():
    
    names = []

    with open(r'C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/Dataset/name_list.txt', 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)

    DIR = r'C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/Dataset'

    haar_cascade = cv.CascadeClassifier('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/MainCode/haar_face.xml')

    features = []
    labels = []

    def create_train():
        for person in names:
            path = os.path.join(DIR, person)
            label =  names.index(person)

            for img in os.listdir(path):
                img_path = os.path.join(path, img)
                print(img_path)

                img_array = cv.imread(img_path)
                gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

                for (x,y,w,h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append(faces_roi)
                    labels.append(label)

    create_train()

    features = np.array(features, dtype = 'object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    #train the recognizer

    face_recognizer.train(features, labels)
    os.chdir('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/MainCode')
    face_recognizer.save('face_trainer.yml')

    np.save('features.npy', features)
    np.save('labels.npy', labels)

    