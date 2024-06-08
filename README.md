

# Project Title: Automated Weapon Detection in Banks and ATMs YOLOv8

## Introduction

This project is focused on custom object detection using the YOLOv8 model. We will annotate our custom dataset using the LabelImg tool, train the model with our annotated data on Google Colab, and finally, implement the trained model in Visual Studio Code for object detection. The objects of interest for this project are knifs, handguns, and longguns.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Data Annotation with LabelImg](#data-annotation-with-labelimg)
- [Training YOLOv8 Model](#training-yolov8-model)
- [Implementing Model in VS Code](#implementing-model-in-vs-code)
- [Image Samples](#image-samples)
- [Conclusion](#conclusion)

## Installation

### Prerequisites
- Python 3.7 or later
- Google Drive account
- Visual Studio Code
- LabelImg tool
- Internet connection for Google Colab

### Step-by-Step Installation

1. **Clone the repository**
    ```sh
    git clone <https://github.com/HarshadNichat/Automated-Weapon-Detection-in-Banks-and-ATMs-.git>
    cd <repository-directory>
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

## Data Annotation with LabelImg

LabelImg is an open-source graphical image annotation tool. It is written in Python and uses Qt for its graphical interface. Follow these steps to annotate your custom dataset:

1. **Download and Install LabelImg**
    ```sh
    pip install labelImg
    ```

2. **Annotate Images**
   - Open LabelImg.
   - Load the directory containing images.
   - Create bounding boxes around objects (knife, handgun, long gun).
   - Save the annotations in XML format ( TXT format (YOLO)).

   This annotated data will be used to train the YOLOv8 model.

3. **Export Annotations**
   - Ensure all annotations are correctly saved in the desired format.
  
# Directory Structure
Dataset Root Directory:
dataset/
     train/
          images/
          labels.txt
     val/
          images/
          labels.txt
Detailed Structure
Training Data:

dataset/train/images/: This directory contains all the images for training.
dataset/train/labels.txt: This file contains the labels for each training image.
Validation Data:

dataset/val/images/: This directory contains all the images for validation.
dataset/val/labels.txt: This file contains the labels for each validation image.

 dataset/
├── train/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── labels.txt
└── val/
    ├── images/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    └── labels.txt


## Training YOLOv8 Model

We will use Google Colab to train our YOLOv8 model with the annotated data.

1. **Prepare Data**
   - Upload your annotated images and annotation files to Google Drive.
   - Grant Google Colab access to your Google Drive.

2. **Set Up Google Colab Environment**
   - Open a new notebook in Google Colab.
   - Install the ultralytics library:
     ```sh
     !pip install ultralytics
     ```

3. **Train the YOLOv8 Model**
   - Import necessary libraries and mount Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

   - Navigate to the directory containing your dataset:
     ```python
     %cd /content/drive/MyDrive/<your-dataset-directory>
     ```

   - Train the model:
     ```python
     from ultralytics import YOLO
     model = YOLO('yolov8n.yaml')
     model.train(data='data.yaml', epochs=30)
     ```

4. **Save the Trained Model**
   - After training, the model will output weights (`best.pt` and `last.pt`).
   - These weights can be found in the specified training directory.

## Implementing Model in VS Code

To utilize the trained YOLOv8 model for detection, follow these steps:

1. **Set Up VS Code**
   - Install the Python extension for Visual Studio Code.
   - Create a new Python environment and activate it.

2. **Load the Trained Model**
   - Copy `best.pt` or `last.pt` to your project directory.

3. **Run Detection Script**
   - Create a Python script to load and run the model:
     ```python
     from ultralytics import YOLO

     model = YOLO('best.pt')
     results = model.predict('path_to_image.jpg')
     results.show()
     ```

4. **Display Results**
   - Ensure the script runs without errors and displays detection results.

## Image Samples


![frame44](https://github.com/HarshadNichat/Automated-Weapon-Detection-in-Banks-and-ATMs-/assets/133520487/c62c6623-b28b-4905-a63c-b456de9d987f)

![knife](https://github.com/HarshadNichat/Automated-Weapon-Detection-in-Banks-and-ATMs-/assets/133520487/e04c7816-e8d6-47ff-8b1a-2ca16b1e5f03)


![longun44](https://github.com/HarshadNichat/Automated-Weapon-Detection-in-Banks-and-ATMs-/assets/133520487/c92f086c-f0f7-408c-b4c6-ddb53fbacd3f)

## Conclusion

This project demonstrates the process of creating a custom object detection model using YOLOv8. From annotating data with LabelImg, training the model on Google Colab, to implementing the model in VS Code, each step is crucial for achieving accurate and efficient object detection. With this guide, you can adapt the methodology to different datasets and objects.

Feel free to contribute to this project by submitting issues or pull requests. For any questions or feedback, please reach out through the project's repository.

Happy coding!
