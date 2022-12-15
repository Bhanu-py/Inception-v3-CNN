import streamlit as st
from PIL import Image
import os
import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import inception_v3

st.title("Vehicle Orientation Assessment")

st.markdown("### 🚗🚘🚔🚖🚍 Classification Application")
st.markdown("This application predicts the orientation of the Vehicle out of 9 Orientations relative to Driver side")
menu = ["Select image from the below list", "Upload From Computer"]
choice = st.sidebar.radio(label="Menu", options=["Select image from the below list", "choose your own image"])
#
if choice == "Select image from the below list":
    file = st.sidebar.selectbox("choose your image", os.listdir("Images"))
    uploaded_file = os.path.join(os.getcwd(), "Images", file)
else:
    uploaded_file = st.sidebar.file_uploader("Please upload an image:", type=['jpeg', 'jpg', 'png'])

# Loading model
### By full model
# model = keras.models.load_model('model/model_optimized')
### By Weights
model = add_new_last_layer(n_classes=9, fc_layer_size=(224, 224, 3))
model.load_weights('top_model_weights.h5')
# print(model.summary())

def predict(img_file):
    """[Predicting whether an image is blur or not]
    Args:
        img_file ([path]): [image file path]
    Returns:
        [string, float]: [Label for the image and also its score]]
    """
    img = Image.open(img_file)
    new_img = np.asarray(img)

    image = keras.preprocessing.image.image_utils.load_img(img_file,
                                                           grayscale=False,
                                                           color_mode="rgb",
                                                           target_size=(224, 224),
                                                           interpolation="nearest", )
    image_array = keras.preprocessing.image.image_utils.img_to_array(image)
    image_array = keras.applications.inception_v3.preprocess_input(image_array, data_format=None)
    input_arr = np.array([image_array])  # Convert single image to a batch.

    classes = {'Driver side front': 0,
               'Driver side rear': 1,
               'Passenger side front': 2,
               'Passenger side rear': 3,
               'Driver side': 4,
               'Front': 5,
               'Passenger side': 6,
               'Rear': 7,
               'Unknown': 8}
    # Label and score prediction based on pre-trained random forest model
    pred = model.predict(input_arr)
    class_label = {i for i in classes if classes[i] == pred.argmax(axis=1)}
    proba = np.max(pred)

    # Label and Score formatting
    pred_class_label = ''.join(class_label)
    pred_score = round(proba, 4)

    # Display image
    st.image(img, caption="Uploaded image", use_column_width=True)

    return pred_class_label, pred_score
# pred_class_label, pred_score = predict('Images/12397.jpg')


if uploaded_file is not None:
    pred_class_label, pred_score = predict(uploaded_file)
    st.write("**Orientation:**", pred_class_label)
    st.write("**Probability:**", f'{round(pred_score*100)}%')
    expander = st.expander("For more details !!")
    expander.write({"Orientation": pred_class_label,
                    "Probability": pred_score})
