import streamlit as st
import pandas as pd
import numpy as np
import sys

import streamlit as st
from PIL import Image

# Set page title
st.set_page_config(page_title="Image Uploader")

# Set page header
st.title("Image Uploader")

# Create an upload button
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image")


print(sys.executable)
