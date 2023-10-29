# Face Recognition System

[![GitHub stars](https://img.shields.io/github/stars/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/network)
[![GitHub license](https://img.shields.io/github/license/adarshkeshri/Face-Recognition-System.svg)](https://github.com/adarshkeshri/Face-Recognition-System/blob/main/LICENSE)

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
This repository contains a real-time Face Recognition System implemented in Python. It uses OpenCV and Haar Cascade files to detect and recognize faces in real-time using a webcam. The system achieves an accuracy of about 90% on the provided dataset.

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

3. Run `Main.py` to start the face recognition system.

4. The system will utilize your webcam to detect and recognize faces in real-time.

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
