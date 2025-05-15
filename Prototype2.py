# backend 
import cv2
import numpy as np


def resize_image(uploaded_file1, size):
    try: 
        # Convert uploaded file to NumPy array using PIL        
        image = np.array(uploaded_file1)
        image2 = image.copy()
        
        if size == "A4":
            img_resize = cv2.resize(image2, (3508,2480))
            print(f"A4 : {img_resize.shape[0:2]}")
        elif size == "website":
            img_resize = cv2.resize(image2, (3508,1280))
            print(f"Website : {img_resize.shape[0:2]}")
        elif size == "potrait":
            img_resize = cv2.resize(image2, (1350,1080))
            print(f"Potrait : {img_resize.shape[0:2]}")
        elif size == "landscape":
            img_resize = cv2.resize(image2, (1920,1080))
            print(f"Landscape : {img_resize.shape[0:2]}")

        cv2.imwrite(r".\EditedImage.jpg", img_resize)
        # print(f"image_edit : {image2}")
        return img_resize

    except Exception as e:
        print(f"Error in rotation : {e}")
        return 0
    
def apply_effect(uploaded_file1, color):
    try: 
        # Convert uploaded file to NumPy array using PIL        
        image = np.array(uploaded_file1)
        image2 = image.copy()
        
        if color == "red":            
            image2[:, :, 0] = 0  # Zero Blue
            image2[:, :, 1] = 0  # Zero Green
        elif color == "green":
            # image2 = image.copy()
            image2[:, :, 0] = 0  # Zero Blue
            image2[:, :, 2] = 0  # Zero Red
        elif color == "blue":
            # image2 = image.copy()
            image2[:, :, 1] = 0  # Zero Green
            image2[:, :, 2] = 0  # Zero Red
        elif color == "gray":
            image2= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif color == "new":
            image2= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        else:
            raise ValueError("Color must be 'red', 'green', or 'blue'.")

        cv2.imwrite(r".\EditedImage.jpg", image2)
        print(f"image_edit : {image2}")
        return image2

    except Exception as e:
        print(f"Error in applying effect : {e}")
        return 0

def rotate(uploaded_file1, direction):
    try: 
        # Convert uploaded file to NumPy array using PIL
        image = np.array(uploaded_file1)
        
        # Rotate based on direction
        if direction == "right":
            rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(r".\EditedImage.jpg", rotated)
            
        elif direction == "left":
            rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(r".\EditedImage.jpg", rotated)
        
        return rotated
    except Exception as e:
        print(f"Error in rotation : {e}")
        return 0
        # main_page.write("No Image Uploaded")


# frontend
import streamlit as st
from PIL import Image
from io import BytesIO

# dividing the window in two horizontal partitions 
# in which sidebar consist of operations that can be performed while main page consist of image
main_page, sidebar = st.columns([0.7,0.3])

# Main Page UI
with main_page:
    st.title("Image Processing Tool")
    st.text("This tool can be used to implement te basic operations on time")

    # widget for uploading the image
    uploaded_file  = st.file_uploader("Please insert the image :", accept_multiple_files=False, type=("png","jpg","svg"),)
    if uploaded_file:
        if "edited_image" not in st.session_state:
            # Load and store original and editable image
            image = Image.open(uploaded_file).convert("RGB")
            st.session_state.edited_image = image.copy()

        st.image(st.session_state.edited_image, caption="Edited Image")
    else:
        st.text("No Image Uploaded")

# SidePage (operations Tab UI)
# sidebar for operations
with sidebar:
    
    with st.container(key="Rotate Container"):
        st.header("Rotate")
        col1, col2 = st.columns([1,1])
            
        with col1:
            if st.button("Rotate Left"):                
                st.session_state.edited_image = rotate(st.session_state.edited_image, "left")                
            
        with col2:
            if st.button("Rotate Right"):
                st.session_state.edited_image = rotate(st.session_state.edited_image, "right")
                # st.experimental_rerun()
        st.divider()     


    # Inject custom CSS
    st.markdown("""
        <style>
            /* Blue Button */
            div[data-testid="stButton"][id="Blue"] button 
            {
                background-color: #007BFF;
                color: white;
            }
            /* Red Button */
            div[data-testid="stButton"][id="Red"] button 
            {
                background-color: #DC3545;
                color: white;
            }
            /* Green Button */
            div[data-testid="stButton"][id="Green"] button 
            {
                background-color: #28A745;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)



    with st.container(key="Adding Effect"):
        st.header("Adding the effect")
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            if st.button(label="Red" ,key="effect_Blue"):
                image = Image.open(uploaded_file).convert("RGB")
                st.session_state.edited_image = apply_effect(image, "blue")                
        
        with col2:
            if st.button(label="Blue" ,key="effect_Red"):
                image = Image.open(uploaded_file).convert("RGB")
                st.session_state.edited_image = apply_effect(image, "red")                               

        with col3:
            if st.button(label="Green" ,key="effect_Green"):
                image = Image.open(uploaded_file).convert("RGB")
                st.session_state.edited_image = apply_effect(image, "green")                

        col4, col5 = st.columns([1,1])
        
        with col4:
            if st.button(label="Gray Scale" ,key="effect_Gray"):
                image = Image.open(uploaded_file).convert("RGB")
                st.session_state.edited_image = apply_effect(image, "gray")

        with col5:
            if st.button(label="New" ,key="effect_New"):
                image = Image.open(uploaded_file).convert("RGB")
                st.session_state.edited_image = apply_effect(image, "new")

        st.divider()




    with st.container(key="Resizing the Image"):
        st.header("Resize Image")
        col1, col2 = st.columns([1,1])

        with col1:
            if st.button("A4 Paper"):
                st.session_state.edited_image = resize_image(st.session_state.edited_image,"A4")
        with col2:
            if st.button("Website"):
                st.session_state.edited_image = resize_image(st.session_state.edited_image,"website")   

        col3, col4 = st.columns([1,1])

        with col3:
            if st.button("Potrait"):
                st.session_state.edited_image = resize_image(st.session_state.edited_image,"potrait")
        with col4:
            if st.button("Landscape"):
                st.session_state.edited_image = resize_image(st.session_state.edited_image,"landscape") 

        st.divider()  


    last_edited_image =  Image.fromarray(st.session_state.edited_image)
    
    img_buffer = BytesIO()
    last_edited_image.save(img_buffer, format="PNG")
    img_buffer.seek(0)  # Move to the beginning of the buffer

    st.download_button(label="Download Image",
    data= img_buffer,
    file_name="my_image.png",
    mime="image/png")