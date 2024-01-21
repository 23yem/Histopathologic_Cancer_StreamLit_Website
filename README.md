# Histopathologic Cancer Detector Machine Learning Project

## Project Description
Hi, I'm Michael and this project is a sophisticated machine learning application focused on histopathologic cancer detection (my second machine learning project). It leverages a Convolutional Neural Network (CNN) model to analyze pathology scans uploaded by users and predict the presence of cancerous cells. The application is developed using Streamlit and TensorFlow and is part of a Kaggle competition aimed at advancing cancer detection methods.

## Key Features
1. **Interactive Web Application**: Developed using Streamlit, this web application allows users to interact with the CNN model seamlessly.
2. **CNN Model for Cancer Detection**: A robust CNN model trained to identify cancerous cells in histopathologic scans.
3. **User Image Upload Interface**: Users can upload their pathology scans via a user-friendly interface on the website.
4. **Real-Time Prediction Display**: The model processes the uploaded images and displays predictions regarding the presence of cancer cells directly on the web application.

## Technical Details
- **Technologies and Libraries**: The project utilizes TensorFlow for model building, NumPy and Pandas for data manipulation, and Streamlit for web deployment.
- **Repository Structure**:
  - `Convolutional_Neural_Network.py`: Main script that integrates the CNN model with the Streamlit application.
  - `data_preprocessing.py`: Script for preprocessing user-uploaded images to be fed into the CNN.
  - `index.py`: Streamlit script for rendering the home page of the web application.
  - HTML Files: Contain the markup for the web pages (`index.html`, `Convolutional_Neural_Network_1.html`, `Convolutional_Neural_Network_2.html`).
  - `model2_saved.h5`: The pre-trained CNN model used for making predictions.
  - `.streamlit/config.toml`: Configuration for Streamlit app appearance and behavior.
  - `requirements.txt`: List of Python dependencies required for the project.

## Learning and Development
- **Model Deployment Skills**: Acquired practical experience in deploying machine learning models to the cloud, making them accessible via a web interface.
- **Streamlit and HTML Integration**: Gained knowledge in integrating HTML with Streamlit and managing user interactions on a web platform.
- **Data Preprocessing for CNN in Cloud**: Learned about the nuances of preparing data for CNN models, especially within a cloud environment.

## Installation and Running the Application
- **Setup Instructions**: Detailed steps to set up the project environment, including installing dependencies listed in `requirements.txt`.
- **Running the App**: Guidance on starting the Streamlit server and accessing the web application locally.

## Repository Links
- [Histopathologic Cancer Detector Streamlit Website](https://github.com/23yem/Histopathologic_Cancer_StreamLit_Website)
- [Kaggle Project Repository](https://github.com/23yem/Kaggle-Histopathologic-Cancer-Detection)

## Additional Resources
- **Kaggle Competition Details**: Information about the Kaggle competition, its objectives, and other submissions.
- **CNN Model Insights**: A deeper dive into the CNN model architecture, training process, and performance metrics.
