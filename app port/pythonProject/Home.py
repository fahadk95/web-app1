import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG-20240404-WA0009.jpg", width=400)

with col2:

    st.title("Fahad Mohammad khan")
    content = """ Hello This is Fahad khan Iam a teacher by profession but
    currently learning to develop some web apps using Python. I have made few apps such as 
    My todo app and image convertor app. This is currently my third app which iam building.
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free 
        to contact me!"""
st.text(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")