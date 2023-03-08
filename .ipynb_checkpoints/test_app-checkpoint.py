import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
search = pickle.load(open('Model_Prediction', 'rb'))

# Define a function for the home page
def home():
    st.title("My Best Position")
    st.subheader("*Where Do I Fit Best On The Pitch??* :face_with_monocle:")
    image = Image.open("ratings.jpg")
    st.image(image, caption='Find Your Best Position in Football', use_column_width=True)
    st.write("")
    st.write("")
    lets_go = st.button("Let's Go!")
    if lets_go:
        st.experimental_rerun()  # Rerun the app to display the second page

# Define a function for the second page with the tabs
def tabs():
    st.title("My Best Position")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality'])
    with tab1:
        image = Image.open("pace.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption="Pace is basically a value that reflects how fast a player's sprint is on the pitch.")

    with tab2:
        image = Image.open("shooting.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption='Shooting is hitting the ball in an attempt to score a goal.')

    with tab3:
        image = Image.open("passing.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption='Passing is the act of transferring the ball to a teammate. It involves accurate delivery of the ball along the ground or in the air.')

    with tab4:
        image = Image.open("dribbling.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption='Dribbling simply means staying on the ball while moving it pass one or more opponents around the pitch.')

    with tab5:
        image = Image.open("defending.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption='Defending in football requires maintaining the correct position, winning tackles and aerial challenges, and efficient play from the back. It is an art.', use_column_width=True)

    with tab6:
        image = Image.open("physicality.jpg")
        size = (300, 300)
        image = image.resize(size)
        st.image(image, caption='Physicality means the ability of player to win the physical battles on the pitch and maintain their fitness throughout a full match.', use_column_width=True)

def compare():
    compare = pd.read_csv('compare.csv')
    player_name = st.text_input('Enter a football player\'s name')
    player = compare.loc[compare['FullName'].str.contains(player_name, case=False)]
    if not player.empty:
        st.write('Name:', player['FullName'].iloc[0])
        st.image(player['PhotoUrl'].iloc[0])
        st.write('Shooting Total:', player['ShootingTotal'].iloc[0])
        st.write('Passing Total:', player['PassingTotal'].iloc[0])
        st.write('Pace Total:', player['PaceTotal'].iloc[0])
        st.write('Defending Total:', player['DefendingTotal'].iloc[0])
        st.write('Dribbling Total:', player['DribblingTotal'].iloc[0])
        st.write('Physicality Total:', player['PhysicalityTotal'].iloc[0])
        st.write('Best Position:', player['BestPosition'].iloc[0])
    else:
        st.write('Player not found')



analysis = pd.read_csv('analysis.csv')

features = ['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal']


def getstarted():
    st.title('How To Rate')
    st.subheader('Summary Statistics and Distribution Plots of Player Ratings by Skill Category')
    getstarted = st.button('Get Started!')
    if getstarted:
        analysis = pd.read_csv('analysis.csv')
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality'])
        
        with tab1:
            st.subheader("the player's overall speed and agility, including sprint speed, acceleration, and agility")
            fig, ax = plt.subplots(figsize=(3,4))
            sns.histplot(data=analysis, x='PaceTotal', kde=False, bins=10)
            ax.set_title('Histogram of PaceTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots(figsize=(6,4))
            sns.kdeplot(data=analysis, x='PaceTotal')
            ax.set_title('Density plot of PaceTotal')
            st.pyplot(fig)
            
        with tab2:
            st.subheader("the player's overall ability to shoot accurately and with power, including finishing, shot power, and long shots")
            fig, ax = plt.subplots()
            sns.histplot(data=analysis, x='ShootingTotal', kde=False, bins=10)
            ax.set_title('Histogram of ShootingTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots()
            sns.kdeplot(data=analysis, x='ShootingTotal')
            ax.set_title('Density plot of ShootingTotal')
            st.pyplot(fig)
        
        with tab3:
            st.subheader("the player's overall ability to pass accurately and effectively, including short passing, long passing, and crossing")
            fig, ax = plt.subplots()
            sns.histplot(data=analysis, x='PassingTotal', kde=False, bins=10)
            ax.set_title('Histogram of PassingTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots()
            sns.kdeplot(data=analysis, x='PassingTotal')
            ax.set_title('Density plot of PassingTotal')
            st.pyplot(fig)
            
        with tab4:
            st.subheader("the player's overall ability to dribble and control the ball, including ball control, dribbling, and agility")
            fig, ax = plt.subplots()
            sns.histplot(data=analysis, x='DribblingTotal', kde=False, bins=10)
            ax.set_title('Histogram of DribblingTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots()
            sns.kdeplot(data=analysis, x='DribblingTotal')
            ax.set_title('Density plot of DribblingTotal')
            st.pyplot(fig)
            
        with tab5:
            st.subheader(" the player's overall ability to defend and tackle, including interceptions, standing tackle, and sliding tackle")
            fig, ax = plt.subplots()
            sns.histplot(data=analysis, x='DefendingTotal', kde=False, bins=10)
            ax.set_title('Histogram of DefendingTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots()
            sns.kdeplot(data=analysis, x='DefendingTotal')
            ax.set_title('Density plot of DefendingTotal')
            st.pyplot(fig)
            
        with tab6:
            st.subheader("the player's overall physical attributes, including strength, stamina, and jumping")
            fig, ax = plt.subplots()
            sns.histplot(data=analysis,  x='PhysicalityTotal', kde=False, bins=10)
            ax.set_title('Histogram of PhysicalityTotal')
            st.pyplot(fig)
            
            fig, ax = plt.subplots()
            sns.kdeplot(data=analysis, x='PhysicalityTotal')
            ax.set_title('Density plot of PhysicalityTotal')
            st.pyplot(fig)  
            
# Create a Streamlit app with multiple pages
PAGES = {"Home": home, "Kick Off": getstarted, "Learn More": tabs, "Player Comparison": compare}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()  # Call the selected page function


st.sidebar.header('Player Attributes')
passing = st.sidebar.slider('PassingTotal', 0, 100)
shooting = st.sidebar.slider('ShootingTotal', 0, 100)
pace = st.sidebar.slider('PaceTotal', 0, 100)
defending = st.sidebar.slider('DefendingTotal', 0, 100)
dribbling = st.sidebar.slider('DribblingTotal', 0, 100)
physicality = st.sidebar.slider('PhysicalityTotal', 0, 100)

new_player = [[passing, shooting, pace, defending, dribbling, defending]]
new_player_df = pd.DataFrame(new_player, columns=['PassingTotal', 'ShootingTotal', 'PaceTotal', 'DefendingTotal', 'DribblingTotal', 'PhysicalityTotal'])

predicted_position = search.predict(new_player_df)
st.header('Prediction Result')
st.write('Based on your attributes, the best position for you is:', predicted_position[0])