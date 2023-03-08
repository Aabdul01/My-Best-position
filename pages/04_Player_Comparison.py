import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

compare = pd.read_csv('Data/compare.csv')
st.subheader("Discover how your favorite football players rate in different attributes and compare them to your predicted best position. Enter any professional football player's name and see how they stack up!")
player_name = st.text_input('Enter a football player\'s name')
player = compare.loc[compare['FullName'].str.contains(player_name, case=False)]
if not player.empty:
    st.write('Name:', player['FullName'].iloc[0])

    st.write('Shooting Total:', player['ShootingTotal'].iloc[0])
    st.write('Passing Total:', player['PassingTotal'].iloc[0])
    st.write('Pace Total:', player['PaceTotal'].iloc[0])
    st.write('Defending Total:', player['DefendingTotal'].iloc[0])
    st.write('Dribbling Total:', player['DribblingTotal'].iloc[0])
    st.write('Physicality Total:', player['PhysicalityTotal'].iloc[0])
    st.write('Best Position:', player['BestPosition'].iloc[0])
else:
    st.write('Player not found')