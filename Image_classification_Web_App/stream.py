# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:34:02 2022

@author: Hariharan.Sivakumar
"""
import streamlit as st


st.title("Image Classification")

st.text("Upload a Image for image classification ")


import keras
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import io
from io import StringIO


model=tf.keras.models.load_model(r"image_model.h5")
class_names = ['benign', 'malignant', 'normal', 'pneumonia']

def read_image(img_path):
    st.write("Classifying...")
    img = img_path
    img = img.resize((224,224),Image.ANTIALIAS)
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    img_array /= 255.
    return img_array


def test_single_image(img_path):
    img_array = read_image(img_path)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print("This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)],
                                                                                          100 * np.max(score)))
    
    st.success("This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)],
                                                                                          100 * np.max(score)))
    return score

    
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg'] )              
if uploaded_file is not None:  
    image = Image.open(uploaded_file)
    st.write("")
    
    img_width, img_height = 224, 224
    test_single_image(image)
