import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
MODEL_PATH = "C:/Users/yashw/Desktop/track_fault_detection/railway_track_fault_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
CLASS_NAMES = ['Defective', 'Non-Defective']

def preprocess_image(image):
    image = image.resize((300, 300))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

st.title("Railway Track Fault Detection")
st.write("Upload an image of a railway track to check for faults.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    
    if prediction[0][0] > 0.5:  # Adjust threshold based on model training
        st.subheader("✅ This Railway track has **NO fault**")
    else:
        st.subheader("❌ This Railway track **HAS a fault**")
