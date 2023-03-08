import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

def tabs():
    st.title("How to Understand Player Ratings: Exploring the Six Key Attributes")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality'])
    with tab1:
        st.write("**Pace**")
        st.write("Pace is a rating that reflects how fast a player can sprint on the pitch. This rating takes into account a player's acceleration, top speed, and agility. A player with a high pace rating can quickly outpace defenders and create scoring opportunities.")
        st.write("0-40: Very slow")
        st.write("40-60: Average or moderate pace")
        st.write("60-75: Very fast")
        st.write("75-100: Exceptionally fast")

    with tab2:
        st.write("**Shooting**")
        st.write("Shooting is the act of kicking the ball towards the goal in an attempt to score. This rating takes into account a player's accuracy, power, and finesse when shooting. A player with a high shooting rating can score from difficult angles or distances and create more scoring opportunities for their team.")
        st.write("0-40: Very poor shooter")
        st.write("40-60: Average or decent shooter")
        st.write("60-75: Very good shooter")
        st.write("75-100: Excellent shooter")
        
    with tab3:
        st.write("**Passing**")
        st.write(" Passing is the act of transferring the ball to a teammate. This rating takes into account a player's accuracy when delivering the ball along the ground or in the air. A player with a high passing rating can create more chances for their team and help them maintain possession of the ball.")
        st.write("0-40: Definitely not a good passer")
        st.write("40-60: Average or good passer")
        st.write("60-75: Very good passer")
        st.write("75-100: Excellent passer")
        
    with tab4:
        st.write("**Dribbling**")
        st.write("Dribbling simply means staying on the ball while moving it past one or more opponents around the pitch. This rating takes into account a player's control and ability to keep the ball close while moving quickly. A player with a high dribbling rating can create space and opportunities for themselves and their teammates.")
        st.write("0-40: Very poor dribbler")
        st.write("40-60: Average or decent dribbler")
        st.write("60-75: Very good dribbler")
        st.write("75-100: Excellent dribbler")
        

    with tab5:
        st.write("**Defending**")
        st.write("Defending in football requires maintaining the correct position, winning tackles and aerial challenges, and efficient play from the back. It is an art. This rating takes into account a player's ability to read the game and anticipate the opposition's movements. A player with a high defending rating can stop the opposition's attacks and protect their team's goal.")
        st.write("0-40: Definitely not a defender")
        st.write("40-60: Average or good defender")
        st.write("60-75: Very good defender")
        st.write("75-100: Excellent defender")
        

    with tab6:
        st.write("**Physicality**")
        st.write("Physicality means the ability of a player to win physical battles on the pitch and maintain their fitness throughout a full match. This rating takes into account a player's strength, stamina, and aggression. A player with a high physicality rating can dominate the midfield and impose themselves on the opposition.")
        st.write("0-40: Very weak physically")
        st.write("40-60: Average or decent physicality")
        st.write("60-75: Very good physicality")
        st.write("75-100: Exceptionally strong")
        
        
tabs()