import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

st.title("My Best Position")
st.subheader("*Where Do I Fit Best On The Pitch??* :face_with_monocle:")
image = Image.open("ratings.jpg")
st.image(image)