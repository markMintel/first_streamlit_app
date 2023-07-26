import streamlit as s
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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
def get_fruityvice_data(this_fruit_choice_:
    fruityive_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
  fruit_choice = s.text_input('What fruit would you like information about?')
  if not fruit_choice:
    s.error('Please select a fruit to get information.')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    s.dataframe(back_from_function)
except URLError as e:
  s.error()

s.stop()

my_cnx = snowflake.connector.connect(**s.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
s.header("The fruit load list contains:")
s.dataframe(my_data_row)

add_my_fruit = s.text_input("What fruit would you like to add?")
s.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
