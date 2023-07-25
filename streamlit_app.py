import streamlit as s
import pandas as pd
import requests

s.title('My Parents New Healthy Diner')

s.header('Breakfast Menu')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, SPinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avacado Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Create a pick list to pick which friuts they want
fruits_selected = s.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
s.dataframe(fruits_to_show)

# Display fruityvice api response

s.header("Fruityvice Fruit Advice!")
fruit_choice = s.text_input('What fruit would you like information about?', 'Kiwi')
s.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalize the json output with pandas
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Put data into a dataframe
s.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
s.text("Hello from Snowflake:")
s.text(my_data_row)
