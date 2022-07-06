
import pandas
import streamlit


streamlit.title('My Parents New healthy Diner')
streamlit.title('This Rocks!! 🎸')

streamlit.header('Breakfast Menu')

streamlit.header('Breakfast Menu 2')

streamlit.text('🍳 Omega 3 and Blueberry Oatmeal')

streamlit.text('🥤 Kale, Spinach and Rocket Smoothie')

streamlit.text('🥚 Hard-Boiled Free-Range Egg')

streamlit.text('🥑 🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries','Grapes'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

# streamlit.dataframe(my_fruit_list)

streamlit.dataframe(fruits_to_show)

# New section to display Fruityvice API response

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvice_response.json())

# Take the json version of the response and normalize it...

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Output it to the screen as a table.

streamlit.dataframe(fruityvice_normalized)


streamlit.text(fruityvice_response)



