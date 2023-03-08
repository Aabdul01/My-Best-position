import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


st.header("Discover Your Best Position")
st.subheader("Adjust the sliders to see the best position for you")
passing = st.slider('PassingTotal', 0, 100)
shooting = st.slider('ShootingTotal', 0, 100)
pace = st.slider('PaceTotal', 0, 100)
defending = st.slider('DefendingTotal', 0, 100)
dribbling = st.slider('DribblingTotal', 0, 100)
physicality = st.slider('PhysicalityTotal', 0, 100)

new_player = [[passing, shooting, pace, defending, dribbling, defending]]
new_player_df = pd.DataFrame(new_player, columns=['PassingTotal', 'ShootingTotal', 'PaceTotal', 'DefendingTotal', 'DribblingTotal', 'PhysicalityTotal'])
getstarted = st.button('Predict!')
if getstarted:
    search = pickle.load(open('Model_Prediction', 'rb'))
    predicted_position = search.predict(new_player_df)
    st.header('Prediction Result')
    st.write('Based on your attributes, the best position for you is:', predicted_position[0])

    positions = {
        'GK': 'Goalkeeper',
        'RB': 'Right Back',
        'CB': 'Centre Back',
        'LB': 'Left Back',
        'RWB': 'Right Wing Back',
        'LWB': 'Left Wing Back',
        'CDM': 'Defensive Midfielder',
        'CM': 'Central Midfielder',
        'CAM': 'Attacking Midfielder',
        'RM': 'Right Midfielder',
        'LM': 'Left Midfielder',
        'RW': 'Right Winger',
        'LW': 'Left Winger',
        'ST': 'Striker',
        'CF': 'Centre Forward'
         }
    predicted_position_full = positions.get(predicted_position[0], 'Unknown')
    st.subheader(predicted_position_full)
