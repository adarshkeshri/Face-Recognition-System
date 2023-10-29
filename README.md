# Face Recognition System

[![GitHub stars](https://img.shields.io/github/stars/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/network)
[![GitHub license](https://img.shields.io/github/license/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/blob/master/LICENSE)

A real-time Face Recognition System implemented in Python using OpenCV and Haar Cascade files.

![Face Recognition System](https://user-images.githubusercontent.com/70345708/94707645-bd0a8e80-0344-11eb-82b7-2350f2ef4f8d.jpg)

## Table of Contents
- [About](#about)
- [Repository Files](#repository-files)
- [Prerequisites](#prerequisites)
- [How to Use](#how-to-use)
- [Training the Model](#training-the-model)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## About
The Face Recognition System is a Python-based real-time facial recognition application that utilizes the power of OpenCV and Haar Cascade files to detect and identify faces through a webcam. With an accuracy rate of approximately 90% on the provided dataset, this system has been designed for various applications, from security and access control to personalized user experiences. The project aims to make face recognition technology accessible and easy to implement in diverse contexts.

## Repository Files
- **Main.py**: The main script to run the face recognition system.
- **face_dataset.py**: Used to capture and store face images for training.
- **face_recog.py**: Performs real-time face recognition.
- **face_train.py**: Trains the recognition model and generates the `face_trainer.yml` file.
- **face_trainer.yml**: Trained face recognition model.
- **features.npy**: Saved facial features.
- **haar_face.xml**: Haar Cascade classifier for face detection.
- **labels.npy**: Labels associated with facial features.
- **name.py**: Script for labeling recognized faces.
- **README.md**: This README file.

## Prerequisites
Before using this system, ensure you have the following installed:
- Python (3.7 or later)
- OpenCV library
- Webcam (for real-time recognition)

## How to Use

1. Clone this repository to your local machine or download the code.

2. Make sure all the required files are in the same directory.

3. Before running the scripts, you may need to customize the file paths according to your system. Here's how you can do that:

   - Open the following files in a text editor and update the file paths where necessary:

     - `Main.py`: You need to specify a different path for the front end pic provided in the repository, you can change it by modifying the `        self.label.setPixmap(QtGui.QPixmap("C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/images.png"))` line.

     - `face_dataset.py`: To specify the folder where you want to store captured face images,you can change it by modifying the `os.chdir('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/Dataset')` and `cv.imwrite('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/Dataset/'+name+'/img'+str(count)+'.png',frame)`.
       
     - `face_recog.py`: Update the following lines in the code to use the `haar_face.xml`,
       `with open(r'C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/Dataset/name_list.txt', 'r') as fp:`,
       `haar_cascade = cv.CascadeClassifier('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/MainCode/haar_face.xml')`,
       `face_recognizer.read('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/MainCode/face_trainer.yml')`.

     - `face_train.py`: Update the following lines in the code to use the `face_trainer.yml` by reading the names from `name_list.txt`,
       `with open(r'C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/Dataset/name_list.txt', 'r') as fp:`,
       `DIR = r'C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/Dataset'`,
       `haar_cascade = cv.CascadeClassifier('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/MainCode/haar_face.xml')`,
       `os.chdir('C:/Users/LENOVOr/Desktop/Project/Face-Recognition-System/MainCode')`.

4. Before running the scripts, you need to install the necessary libraries. You can do this using `pip`:
   - `pip install opencv-contrib-python`

5. Run `Main.py` to start the face recognition system.

6. The system will utilize your webcam to detect and recognize faces in real-time.
   

## Training the Model
If you want to retrain the model or add new faces for recognition, follow these steps:
1. Run `face_dataset.py` to capture and store face images.
2. Run `face_train.py` to train the recognition model.

## Customization
You can customize the system by modifying the code to fit your specific use case, such as changing the recognition accuracy or adding new faces for training.

## Contributing
If you encounter any issues or have suggestions for improvement, please open an issue or contribute to the project. We welcome contributions from the open-source community.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy using the Face Recognition System!
