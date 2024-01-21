import numpy as np 
import random
import os

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



# Set Global random seed to make sure we can replicate any model that we create (no randomness)
np.random.seed(42)
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)


os.environ['TF_DETERMINISTIC_OPS'] = '1'

#This is a function to crop the image to focus on the 32x32px center of the image. We will call this function in the ImageDataGenerator() function
def crop_center(img): 
    y, x, _ = img.shape
    startx = x//2 - (32//2)
    starty = y//2 - (32//2)    
    return img[starty:starty+32, startx:startx+32, :]



# This is to take the path of the image and save it in a dataframe, along with it's label
def Image_Path_to_DataFrame():
   
    # Dataframe with two columns: one with id and one with the path to the image. This is the format in which we can pass into the ImageGenerator (for data augmentation)
    labels = pd.DataFrame({
        'id': ["uploaded_img.tif"],
        'path': ["uploaded_img.tif"] # Streamlit runs from the Histopathologic_Cancer_StreamLit_Website directory, so no need to do Histopathologic_Cancer_StreamLit_Website/uploaded_img.tif"
    })

    return labels



# Turn DataFrame into a ImageDataGenerator which is then turned into a data generator via the .flow_from_dataframe().
def DataFrame_to_DataGenerator():

    # Creating an instance of the ImageDataGenerator for data augmentation and preprocessing
    input_datagen = ImageDataGenerator(
        rescale=1./255,  # Rescale the image pixel values to [0,1]
        preprocessing_function = crop_center  # call the crop function on each image
    )


    # Flow from dataframe method to load images using the dataframe
    input_generator = input_datagen.flow_from_dataframe(
        dataframe = Image_Path_to_DataFrame(),  # Use the Dataframe which we store info about the uploaded image
        x_col='path',
        y_col=None, # We don't have labels for the input data. we are trying to predict the label (outcome)
        target_size=(32, 32),  # The dimensions to which all images found will be resized. Change this as needed
        color_mode='rgb',
        class_mode=None,  # Set class_mode to None since there are no labels in this data
        batch_size=1, # only one image in this case, so we can just set batch size to 1
        seed=42
    )
    # Now you have transformed your data into a format which the Convolutional Neural Network will be able to process and make a prediction based on

    return input_generator


def data_preprocessing():
    # Get the generator
    generator = DataFrame_to_DataGenerator()

    return generator


print(data_preprocessing())
