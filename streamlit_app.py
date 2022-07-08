import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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


# Function code block to follow:

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  # Take the json version of the response and normalize it...
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# New section to display Fruityvice API response

streamlit.header("Fruityvice Fruit Advice!")
try:
  # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # Take the json version of the response and normalize it...
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    
    
    # Output it to the screen as a table.
    # streamlit.dataframe(fruityvice_normalized)
    
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  streamlit.error()
  
  
  # streamlit.write('The user entered ', fruit_choice)
  # import requests
  #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  #streamlit.text(fruityvice_response)
  #streamlit.text(fruityvice_response.json())



# Stop running whilst we debug...
streamlit.stop()

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.header("Fruit list:")
# streamlit.dataframe(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit list:")
streamlit.dataframe(my_data_rows)

fruit_to_add = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered ', fruit_to_add)

my_cur.execute("insert into fruit_load_list values ('From Streamlit')")




