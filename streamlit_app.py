import streamlit
import pandas 
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')


streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text(':blueberries: Omega 3 & Blueberry Oatmeal')

streamlit.dataframe(my_fruit_list)
