#!/usr/bin/env python
# coding: utf-8

# # Exercise - Bar Charts and Heatmaps
# 
# In this exercise, you will use your new knowledge to propose a SimulationSimulationsolution to a real-world scenario.  To succeed, you will need to import data into Python, answer questions using the data, and generate **bar charts** and **heatmaps** to understand patterns in the data.
# 
# ## Scenario
# 
# You've recently decided to create your very own video game!  As an avid reader of [IGN Game Reviews](https://www.ign.com/reviews/games), you hear about all of the most recent game releases, along with the ranking they've received from experts, ranging from 0 (_Disaster_) to 10 (_Masterpiece_).
# 
# ![ex2_ign](https://i.imgur.com/Oh06Fu1.png)
# 
# You're interested in using [IGN reviews](https://www.ign.com/reviews/games) to guide the design of your upcoming game.  Thankfully, someone has summarized the rankings in a really useful CSV file that you can use to guide your analysis.
# 
# ## Setup
# 
# Run the next cell to import and configure the Python libraries that you need to complete the exercise.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## Step 1: Load the data
# 
# Read the IGN data file into `ign_data`.  Use the `"Platform"` column to label the rows.

# In[2]:


ign_data = pd.read_csv('kaggle data/ign_scores.csv', index_col='Platform')


# ## Step 2: Review the data
# 
# Use a Python command to print the entire dataset.

# In[3]:


ign_data


# The dataset that you've just printed shows the average score, by platform and genre.  Use the data to answer the questions below.

# In[4]:


# Fill in the line below: What is the highest average score received by PC games,
# for any platform?
high_score = 7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'


# ## Step 3: Which platform is best?
# 
# Since you can remember, your favorite video game has been [**Mario Kart Wii**](https://www.ign.com/games/mario-kart-wii), a racing game released for the Wii platform in 2008.  And, IGN agrees with you that it is a great game -- their rating for this game is a whopping 8.9!  Inspired by the success of this game, you're considering creating your very own racing game for the Wii platform.
# 
# #### Part A
# 
# Create a bar chart that shows the average score for **racing** games, for each platform.  Your chart should have one bar for each platform. 

# In[7]:


# Bar chart showing average score for racing games by platform
plt.figure(figsize=(14,6))# Your code here
plt.title('Average Score for Racing Games, by Platform')
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
plt.xlabel('Socres ')


# #### Part B
# 
# Based on the bar chart, do you expect a racing game for the **Wii** platform to receive a high rating?  If not, what gaming platform seems to be the best alternative?

# **Solution**:- No, Wii platform does not receive a high rating, if we see bar chart for Racing Game Xbox One platform has highest rating instead of Wii.
# 
# Thank you.

# ## Step 4: All possible combinations!
# 
# Eventually, you decide against creating a racing game for Wii, but you're still committed to creating your own video game!  Since your gaming interests are pretty broad (_... you generally love most video games_), you decide to use the IGN data to inform your new choice of genre and platform.
# 
# #### Part A
# 
# Use the data to create a heatmap of average score by genre and platform.  

# In[14]:


plt.figure(figsize=(12,8))
plt.title('Heatmap for average game score by plotform and gener')
sns.heatmap(data=ign_data, annot = True)
plt.xlabel('gener')


# #### Part B
# 
# Which combination of genre and platform receives the highest average ratings?  Which combination receives the lowest average rankings?

# **Solutio**:- After lokking heatmap it's clear that gener-Simulation , and platform-playstation4 has highest average rating while two gener-Shooter,Fighting of same platform-Game Boy Color, have lowest average rating.
# 
# thank you.

# # Keep going
# 
# Move on to learn all about **[scatter plots](https://www.kaggle.com/alexisbcook/scatter-plots)**!

# In[ ]:




