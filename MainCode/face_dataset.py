import cv2 as cv
import os

def dataset(name):

    os.chdir('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/Dataset')

    if not os.path.exists(name):
        os.mkdir(name)
        with open('name_list.txt', 'a') as fp:
            fp.write(name+"\n")

    camera = cv.VideoCapture(0)

    count = 0

    while count<100:
        status, frame = camera.read()

        if not status:
            print("Frame is not been captured..Exiting...")
            break
        cv.imshow("Video Window",frame)

        cv.imwrite('C:/Users/KIIT/Desktop/VSCoding/Projects/FaceRecognition/Dataset/'+name+'/img'+str(count)+'.png',frame)

        count=count+1
        if cv.waitKey(1) == ord('q'):
            break

    camera.release()
    cv.destroyAllWindows()