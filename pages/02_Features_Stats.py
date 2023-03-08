import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

analysis = pd.read_csv('analysis.csv')

features = ['PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal']


def getstarted():
    st.subheader('Summary Statistics and Distribution Plots of Player Ratings by Skill Category')
    analysis = pd.read_csv('analysis.csv')
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality'])

    with tab1:
        st.write("Analyzing the overall speed and agility of players, including sprint speed, acceleration, and agility. This analysis includes a histogram and density plot of the PaceTotal variable, showing the distribution of speed and acceleration among players. Additionally, a box plot is included to compare the PaceTotal variable across different player positions. Finally, a summary table is provided, which includes key statistics such as the average, standard deviation, maximum, minimum, and mode of the PaceTotal variable.")
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='PaceTotal', kde=False, bins=10)
            ax.set_title('Histogram of PaceTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='PaceTotal')
            ax.set_title('Density plot of PaceTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='PaceTotal')
            ax.set_title('Box plot of PaceTotal')
            st.pyplot(fig)
        with col2:            
            mean = analysis.PaceTotal.mean()
            STD = analysis.PaceTotal.std()
            Max = analysis.PaceTotal.max()
            Min = analysis.PaceTotal.min()
            common = analysis.PaceTotal.mode().tolist()

            pace = {
             'Average': [mean],
             'STD': [STD],
             'Max': [Max],
             'Min': [Min],
             'Mode': [common]
               }
            pace_df = pd.DataFrame(pace)
            st.dataframe(pace_df)
        
    with tab2:
        st.write("This analysis focuses on evaluating the accuracy and power of players' shooting abilities, including their finishing, shot power, and long shots. It includes a histogram and density plot of the ShootingTotal variable to showcase the distribution of shooting skills among players. Moreover, a box plot is included to compare the ShootingTotal variable across various player positions. Finally, a summary table is provided, which displays key statistics such as the average, standard deviation, maximum, minimum, and mode of the ShootingTotal variable.")
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='ShootingTotal', kde=False, bins=10)
            ax.set_title('Histogram of ShootingTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='ShootingTotal')
            ax.set_title('Density plot of ShootingTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='ShootingTotal')
            ax.set_title('BoxPlot of ShootingTotal')
            st.pyplot(fig)
        with col2:
            mean = analysis.ShootingTotal.mean()
            STD = analysis.ShootingTotal.std()
            Max = analysis.ShootingTotal.max()
            Min = analysis.ShootingTotal.min()
            common = analysis.ShootingTotal.mode().tolist()
        
            shooting = {
              'Average': [mean],
              'STD': [STD],
              'Max': [Max],
              'Min': [Min],
              'Mode': [common]
                }
            shooting_df = pd.DataFrame(shooting)
            shooting_df
            st.dataframe(shooting_df)
            
    with tab3:
        st.write("This section focuses on the players' ability to pass the ball accurately and efficiently, including short, long, and cross passes. The analysis includes a histogram and density plot of the PassingTotal variable, demonstrating the distribution of passing ability among players. Additionally, a box plot is presented to compare the PassingTotal variable across different player positions, providing insights into how different positions may require varying degrees of passing ability. Finally, a summary table is included, which displays key statistics such as the mean, standard deviation, maximum, minimum, and mode of the PassingTotal variable.")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='PassingTotal', kde=False, bins=10)
            ax.set_title('Histogram of PassingTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='PassingTotal')
            ax.set_title('Density plot of PassingTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='PassingTotal')
            ax.set_title('BoxPlot of PassingTotal')
            st.pyplot(fig)
        with col2:
            mean = analysis.PassingTotal.mean()
            STD = analysis.PassingTotal.std()
            Max = analysis.PassingTotal.max()
            Min = analysis.PassingTotal.min()
            common = analysis.PassingTotal.mode().tolist()

            passing = {
               'Average': [mean],
               'STD': [STD],
               'Max': [Max],
               'Min': [Min],
               'Mode': [common]
                }
            passing_df = pd.DataFrame(passing)
            st.dataframe(passing_df)
            
    with tab4:
        st.write("This analysis focuses on the players' dribbling ability, encompassing factors such as ball control, dribbling speed, and dribbling accuracy. The distribution of the DribblingTotal variable is illustrated by a histogram and density plot, providing insight into the players' overall dribbling skills. A box plot is also included to compare the DribblingTotal variable across different player positions, highlighting any differences in the players' dribbling ability based on their positions. Finally, a summary table presents key statistics such as the average, standard deviation, maximum, minimum, and mode of the DribblingTotal variable.")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='DribblingTotal', kde=False, bins=10)
            ax.set_title('Histogram of DribblingTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='DribblingTotal')
            ax.set_title('Density plot of DribblingTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='DribblingTotal')
            ax.set_title('BoxPlot of DribblingTotal')
            st.pyplot(fig)
        with col2:
            mean = analysis.DribblingTotal.mean()
            STD = analysis.DribblingTotal.std()
            Max = analysis.DribblingTotal.max()
            Min = analysis.DribblingTotal.min()
            common = analysis.DribblingTotal.mode().tolist()

            dribbling = {
              'Average': [mean],
              'STD': [STD],
              'Max': [Max],
              'Min': [Min],
              'Mode': [common]
               }
            dribbling_df = pd.DataFrame(dribbling)
            st.dataframe(dribbling_df)
            
    with tab5:
        st.write("This analysis delves into the overall defensive abilities of players, focusing on attributes such as standing tackle, sliding tackle, and interceptions. A histogram and density plot of the DefendingTotal variable is included, providing an overview of the distribution of these skills among the players. The analysis also incorporates a box plot, enabling a comparison of the DefendingTotal variable across various player positions. Finally, a summary table is included, presenting essential statistics such as the average, standard deviation, maximum, minimum, and mode of the DefendingTotal variable.")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='DefendingTotal', kde=False, bins=10)
            ax.set_title('Histogram of DefendingTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='DefendingTotal')
            ax.set_title('Density plot of DefendingTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='DefendingTotal')
            ax.set_title('BoxPlot of DefendingTotal')
            st.pyplot(fig)
        with col2:
            mean = analysis.DefendingTotal.mean()
            STD = analysis.DefendingTotal.std()
            Max = analysis.DefendingTotal.max()
            Min = analysis.DefendingTotal.min()
            common = analysis.DefendingTotal.mode().tolist()

            defending = {
              'Average': [mean],
              'STD': [STD],
              'Max': [Max],
              'Min': [Min],
              'Mode': [common]
              }
            defending_df = pd.DataFrame(defending)
            st.dataframe(defending_df)
            
    with tab6:
        st.write("This analysis focuses on the physicality of players, including their strength, stamina, and body balance. It includes a histogram and density plot of the PhysicalityTotal variable, illustrating the distribution of physicality attributes among players. Additionally, a box plot is provided to compare the PhysicalityTotal variable across different player positions. Finally, a summary table is included, containing key statistics such as the mean, standard deviation, maximum, minimum, and mode of the PhysicalityTotal variable.")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.histplot(data=analysis, x='PhysicalityTotal', kde=False, bins=10)
            ax.set_title('Histogram of PhysicalityTotal')
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.kdeplot(data=analysis, x='PhysicalityTotal')
            ax.set_title('Density plot of PhysicalityTotal')
            st.pyplot(fig)
        col1, col2, = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize =(10, 8))
            sns.boxplot(data=analysis, x='BestPosition', y='PhysicalityTotal')
            ax.set_title('BoxPlot of PhysicalityTotal')
            st.pyplot(fig)
        with col2:
            mean = analysis.PhysicalityTotal.mean()
            STD = analysis.PhysicalityTotal.std()
            Max = analysis.PhysicalityTotal.max()
            Min = analysis.PhysicalityTotal.min()
            common = analysis.PhysicalityTotal.mode().tolist()

            physicality = {
                'Average': [mean],
                'STD': [STD],
                'Max': [Max],
                'Min': [Min],
                'Mode': [common]
              }
            physicality_df = pd.DataFrame(physicality)
            st.dataframe(physicality_df)
        
getstarted()
