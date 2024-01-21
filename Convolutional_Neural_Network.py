from PIL import Image
import io

import streamlit as st
from streamlit.components import v1 as components
import tensorflow as tf
from tensorflow.keras.models import load_model

from data_preprocessing import data_preprocessing

st.set_page_config(layout="wide")

# Load HTML file
with open('Convolutional_Neural_Network_1.html', 'r') as file:    
    html_content = file.read()

components.html(html_content, width = None, height=1100)

#Add some spacing between elements on the website
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.markdown("""
    <style>
    .element-container {
        margin-bottom: 0px;
    }
    .stSlider, .stSelectbox {
        padding-bottom: 10px;
    }
    .stMarkdown {
        padding-bottom: 1px;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <div style="text-align: center">
        <h1>Using my best Deployed and Saved Convolutional Neural Network</h1>
        <h4>1. Press the "Random" Button, which will give you a random pathology scan image with potential cancer. </h4>
        <h4>2. Once you press the "Random" button, a "Download TIFF image" button will also appear, allowing you to download the image.</h4>
        <h4>3. Continue to press the "Random" button if you want to switch images.</h4>
        <h4>4. Once you find one you like, download it using the "Download TIFF image" button and then upload via the "Browse files" button. It will  then display the image you uploaded.</h4>
        <h4>5. Once you uploaded the .tif file, press the "Predict" button and then you will see if your photo contains cancer, using my deployed machine learning model.</h4>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

import os
import random

# Create a column layout so the text below is less wide
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col3:
    st.write("")
    
# User input for each feature
with col2:

    st.write("")

      # Make the buttons bigger
    st.markdown("""
        <style>
        .stButton>button {
            font-size: 10px;
            padding: 20px 40px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Button to select a random image
    if st.button('Random'):

        # Directory containing the TIFF images
        img_dir = "images"

        # Get a list of all TIFF images in the directory
        img_files = [f for f in os.listdir(img_dir) if f.endswith('.tif')]

        # Select a random image file
        img_file = random.choice(img_files)

        # Read the selected image file into a bytes object
        with open(os.path.join(img_dir, img_file), "rb") as f:
            img_bytes = f.read()

            

        # Display the selected image
        st.image(img_bytes, caption='Your Image', use_column_width=False)

        # Create a download button for the selected image
        st.download_button(
            label="Download TIF image",
            data=img_bytes,
            file_name=img_file,
            mime="image/tiff"
        )


    # File uploader for the user to upload their image
    uploaded_file = st.file_uploader("Choose an image...", type=["tif", "tiff"])

    # If an image is uploaded
    if uploaded_file is not None:

        # Read the uploaded image into a bytes object
        uploaded_img_bytes = uploaded_file.read()

        # Convert the uploaded image bytes to a PIL Image
        uploaded_img = Image.open(io.BytesIO(uploaded_img_bytes))

        # Convert the PIL Image to TIF and save it
        uploaded_img.save("uploaded_img.tif")

        # Display the uploaded image
        st.image(uploaded_img_bytes, caption='Your Uploaded Image', use_column_width=False)




    def predictions():
        # Load the saved model
        model = tf.keras.models.load_model(os.path.join("model2_saved.h5"))

        preprocessed_img = data_preprocessing()

        # Make a prediction
        prediction = model.predict(preprocessed_img, steps = len(preprocessed_img))

        return prediction



    # Button to make a prediction
    if st.button('Predict'):
        # If an image is uploaded
        if uploaded_file is not None:
            # Preprocess the uploaded image
            
            prediction = predictions()

            prediction_float = round(prediction[0][0] * 100, 2)  # change it to a percentage, rounded to the hundreth

            # Display the prediction
            if prediction_float >= 50:
                st.markdown(f'#### Prediction: <span style="color: red; font-weight: bold;">The model predicts that this image contains cancer</span>, with a {prediction_float}% chance of cancer', unsafe_allow_html=True)
            else:
                st.markdown(f'#### Prediction: <span style="color: green; font-weight: bold;">The model predicts that this image does not contain cancer</span>, with a {prediction_float}% chance of cancer', unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='text-align: center; color: red;'>Please upload an image first.</h4>", unsafe_allow_html=True) # If there is no uploaded photo

    # def predict(pclass, sex, fare, age, sibsp, parch):
    #     # Convert inputs to model's expected format
    #     pclass = int(pclass)
    #     sex = str(sex)
    #     fare = float(fare)
    #     age = float(age)
    #     sibsp = int(sibsp)
    #     parch = int(parch)


    #     # Prepare the input data in the correct format

    #     preprocessed_data = data_preprocessing(pclass, sex, fare, age, sibsp, parch)

    #     model12 = load_model("model_12_saved.h5")

    #     # Make prediction
    #     prediction = model12.predict(preprocessed_data)
        
    #     return prediction


    # # Make the button bigger
    # st.markdown("""
    #     <style>
    #     .stButton>button {
    #         font-size: 10px;
    #         padding: 20px 40px;
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)

    # if st.button('Predict'):
    #     prediction_float = predict(pclass, sex, fare, age, sibsp, parch)
    #     prediction_float = round(prediction_float[0][0] * 100, 2)    # turn to a percentage and round to the nearest hundreth

    #     if prediction_float > 50:
    #         st.markdown(f'#### Prediction: <span style="color: green; font-weight: bold;">Your person would have survived the titanic</span>, with a survival rate of {prediction_float}%', unsafe_allow_html=True)
    #     else:
    #         st.markdown(f'#### Prediction: <span style="color: red; font-weight: bold;">Your person would not have survived the titanic</span>, with only a survival rate of {prediction_float}%', unsafe_allow_html=True)





# Load part 2
with open('Convolutional_Neural_Network_2.html', 'r') as file:    
    html_content_2 = file.read()

components.html(html_content_2, width = None, height=5500)