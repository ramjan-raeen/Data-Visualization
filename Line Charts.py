#!/usr/bin/env python
# coding: utf-8

# # Exercise - Line Charts
# In this exercise, you will use your new knowledge to propose a solution to a real-world scenario. To succeed, you will need to import data into Python, answer questions using the data, and generate **line charts** to understand patterns in the data.

# ## Scenario
# 
# You have recently been hired to manage the museums in the City of Los Angeles. Your first project focuses on the four museums pictured in the images below.
# 
# ![ex1_museums](https://i.imgur.com/pFYL8J1.png)
# 
# You will leverage data from the Los Angeles [Data Portal](https://data.lacity.org/) that tracks monthly visitors to each museum.  
# 
# ![ex1_xlsx](https://i.imgur.com/mGWYlym.png)
# 
# ## Setup
# Run the next cell to import and configure the Python libraries that you need to complete the exercise.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## Step 1: Load the data
# 
# Your first assignment is to read the LA Museum Visitors data file into `museum_data`.  Note that:
# - The filepath to the dataset is stored as `museum_filepath`.  Please **do not** change the provided value of the filepath.
# - The name of the column to use as row labels is `"Date"`.  (This can be seen in cell A1 when the file is opened in Excel.)
# 
# To help with this, you may find it useful to revisit some relevant code from [the tutorial](https://www.kaggle.com/alexisbcook/hello-seaborn):
# 
# ```python
# # Path of the file to read
# data_museum = "kaggle data/museum_visitors.csv"
# 
# # Read the file into a variable spotify_data
# museum_data = pd.read_csv(data_museum, index_col="Date", parse_dates=True)
# ```
# 
# The code you need to write now looks very similar to above!

# In[2]:


museum_data = pd.read_csv('kaggle data/museum_visitors.csv', index_col = "Date", parse_dates = True)


# ## Step 2: Review the data
# 
# Use a Python command to print the last 5 rows of the data.

# In[3]:


museum_data.tail()


# The last row (for `2018-11-01`) tracks the number of visitors to each museum in November 2018, the next-to-last row (for `2018-10-01`) tracks the number of visitors to each museum in October 2018, _and so on_.
# 
# Use the last 5 rows of the data to answer the questions below.

# In[4]:


# Fill in the line below: How many visitors did the Chinese American Museum receive in July 2018?

ca_museum_jul18 =2620

# Fill in the line below: In October 2018, how many more visitors did Avila 
# Adobe receive than the Firehouse Museum?
avila_oct18 = 19280 - 4622


#  ## Step 3: Convince the museum board 
#  ![](http://)
# 
# The Firehouse Museum claims they ran an event in 2014 that brought an incredible number of visitors, and that they should get extra budget to run a similar event again.  The other museums think these types of events aren't that important, and budgets should be split purely based on recent visitors on an average day.  
# 
# To show the museum board how the event compared to regular traffic at each museum, create a line chart that shows how the number of visitors to each museum evolved over time.  Your figure should have four lines (one for each museum).
# 
# > **(Optional) Note**: If you have some prior experience with plotting figures in Python, you might be familiar with the `plt.show()` command.  If you decide to use this command, please place it **after** the line of code that checks your answer (in this case, place it after `step_3.check()` below) -- otherwise, the checking code will return an error!

# In[5]:


# Line chart showing the number of visitors to each museum over time
plt.figure(figsize=(18,8))
plt.title('Monthly Visitors to Los Angeles City Museum')
sns.lineplot(data = museum_data)
plt.xlabel('Date')


# ## Step 4: Assess seasonality
# 
# When meeting with the employees at Avila Adobe, you hear that one major pain point is that the number of museum visitors varies greatly with the seasons, with low seasons (when the employees are perfectly staffed and happy) and also high seasons (when the employees are understaffed and stressed).  You realize that if you can predict these high and low seasons, you can plan ahead to hire some additional seasonal employees to help out with the extra work.
# 
# #### Part A
# Create a line chart that shows how the number of visitors to Avila Adobe has evolved over time.  (_If your code returns an error, the first thing that you should check is that you've spelled the name of the column correctly!  You must write the name of the column exactly as it appears in the dataset._)

# In[6]:


## Line plot showing the number of visitors to Avila Adobe over time
plt.figure(figsize=(18,6))
plt.title('Line Char of Visitors to Avila Adobe over time')
sns.lineplot(data= museum_data['Avila Adobe'], label='Avila Adove')
plt.xlabel('Date')


# #### Part B
# 
# Does Avila Adobe get more visitors:
# - in September-February (in LA, the fall and winter months), or 
# - in March-August (in LA, the spring and summer)?  
# 
# Using this information, when should the museum staff additional seasonal employees?

# **Solution**:- The line chart generally little complex to see but you obseve more, you will find that in each year the values are low around in December and january and the values are highest in middle of year i.e around May and June. The you can say that Avila Adobe usually gets more visitors in March- August (or the spring and summer months) and Avila Adobe could definitely benefit from hiring more seasonal employees to help with the extra work in March- August (Or the sprig and summer).
# 
# Thank you.

# In[ ]:




