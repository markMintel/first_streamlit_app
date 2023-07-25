import streamlit as s
import pandas as pd

s.title('My Parents New Healthy Diner')

s.header('Breakfast Menu')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, SPinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avacado Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
s.dataframe(my_fruit_list)
