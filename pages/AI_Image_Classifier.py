import base64
import keras
import tensorflow as tf
import streamlit as st
import cv2 as cv
from PIL import Image, ImageOps
import numpy as np

image_size = (180, 180)

page_by_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://codehs.com/uploads/805e86e0c8090b04e92c97d593b0ff3a");
    background-size: cover;
    }
    </style>
"""


st.markdown(page_by_img, unsafe_allow_html=True)

@st.cache_data
def load_image(image_file):
  image = Image.open(image_file)
  return image

def load_model(model):
  model = tf.keras.models.load_model(model)
  return model
with st.spinner('Loading Model, Please Wait..'):
  model=load_model("pages/classification_model.keras")

def import_and_predict(image, model):
  size = image_size   
  image = ImageOps.fit(image, size, Image.LANCZOS)
  image = np.asarray(image)
  img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  img_reshape = img[np.newaxis,...]
  prediction = model.predict(img_reshape)
  return prediction

file = st.file_uploader("Please upload an image!", type=["jpg", "png"])

if file is None:
  st.text("Please upload an image! (file type: .jpg, .png)")
else:
  final_decision = ""
  image = load_image(file)
  st.image(image, use_container_width=True)
  predictions = import_and_predict(image, model)
  score = float(keras.ops.sigmoid(predictions[0][0]))

  fake_percentage = 100 * (1 - score)

  real_percentage = 100 * score
        
  if fake_percentage > real_percentage + 10:
      st.write(f" #### This image is most likely AI-generated! (Model confidence: {100 * (1 - score):.2f}% )")
      final_decision = "AI-Generated"
  elif real_percentage > fake_percentage + 10:
    st.write(f" #### This image is most likely human generated! (Model confidence: {100 * score:.2f}%)")
    final_decision = "Human-Generated"
  else:
    st.write(f" #### The model can not confidently determine whether this image is AI- or human-generated ({100 * (1 - score):.2f}% AI-Gen and {100 * score:.2f}% Human-Gen)")
    final_decision = "Undetermined"