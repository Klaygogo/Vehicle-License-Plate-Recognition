# Vehicle-License-Plate-Recognition

## Overview

This repository contains the code and documentation for a license plate segmentation system based on the YOLOv8 model. The system is designed to accurately detect and segment license plates from various traffic scenes, providing a crucial input for intelligent traffic systems.

## Dataset

The system utilizes two datasets for training and testing:

1. **CCPD2020**: Contains 11,774 images of new energy vehicle license plates.
2. **CCPD2019**: Consists of two subsets with 20,967 images of regular fuel vehicle (blue plate) and 25,467 images of fuel vehicles with higher recognition difficulty (blurry, high tilt, etc.).

## Data Preprocessing

The `plate_dataset_preprocess.py` script is responsible for preparing the CCPD datasets for training the YOLOv8 model. The script performs the following tasks:

- Extracts车牌位置信息 from image filenames.
- Creates corresponding label (.txt) files for each image, including class labels (blue plate as 1, green plate as 0), plate center coordinates, and plate dimensions.
- Splits the dataset into training, validation, and testing sets in a 5:3:2 ratio.

## Model Training

The `model.py` script is used to train and use the YOLOv8 model on the preprocessed dataset. The training process involves:

- Loading the pre-trained YOLOv8 model.
- Adjusting hyperparameters such as learning rate, batch size, and number of epochs.
- Monitoring loss functions to ensure optimal model performance.
