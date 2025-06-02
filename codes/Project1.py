# backend
import cv2
import numpy as np
from PIL import Image

def rotate(image_pil, direction):
    try:
        # Convert PIL image to NumPy array
        image_np = np.array(image_pil)

        # Convert RGB to BGR for OpenCV operations if needed
        if image_np.shape[2] == 3:  # Check for 3 channels
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # Rotate based on direction
        if direction == "right":
            rotated_np = cv2.rotate(image_np, cv2.ROTATE_90_CLOCKWISE)
        elif direction == "left":
            rotated_np = cv2.rotate(image_np, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            return image_pil  # Return original if unknown direction

        # Convert back to RGB and then to PIL
        rotated_np = cv2.cvtColor(rotated_np, cv2.COLOR_BGR2RGB)
        rotated_pil = Image.fromarray(rotated_np)

        return rotated_pil
    except Exception as e:
        print("Error in rotation:", e)
        return image_pil

# frontend
import streamlit as st

# dividing the window in two horizontal partitions 
main_page, sidebar = st.columns([0.7,0.3])

# Main Page UI
with main_page:
    st.title("Image Processing Tool")
    st.text("This tool can be used to implement the basic operations on image")

    uploaded_file = st.file_uploader("Please insert the image:", type=("png", "jpg", "jpeg"))

    if uploaded_file:
        if "edited_image" not in st.session_state:
            # Load and store original and editable image
            image = Image.open(uploaded_file).convert("RGB")
            st.session_state.edited_image = image.copy()

        st.image(st.session_state.edited_image, caption="Edited Image", use_column_width=True)
    else:
        st.text("No Image Uploaded")

# Sidebar (Operations Tab UI)
with sidebar:
    st.header("Rotate")
    col1, col2 = st.columns(2)

    if uploaded_file:
        with col1:
            if st.button("Rotate Left"):
                st.session_state.edited_image = rotate(st.session_state.edited_image, "left")
                st.experimental_rerun()

        with col2:
            if st.button("Rotate Right"):
                st.session_state.edited_image = rotate(st.session_state.edited_image, "right")
                st.experimental_rerun()
