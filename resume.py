from pathlib import Path as p
import streamlit as st
from PIL import Image
current=p.cwd()
css=r"C:\Program Files\Python38\styles\main.css.txt"
PAGE_TITLE ="Digital CV | Kalash Gulati"
PAGE_ICON = ":wave:"
NAME = "Kalash Gulati"
DESCRIPTION = "Senior Data Analyst, assisting enterprises by supporting data-driven"
EMAIL = "gulatikalash05@gmail.com"
SOCIAL_MEDIA = {"Youtube":r"https://www.youtube.com/@kalashgulati9265/videos","insta":r"https://www.instagram.com/thesanskariigulati/","GITHUB" : r"https://github.com/failedengineers"}
PROJECTS={"VRITUAL AI":r"https://github.com/failedengineers/virtual-ai"}
st.set_page_config(page_title=PAGE_TITLE ,page_icon=PAGE_ICON)



col1=st.columns(1)
with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(":email:",EMAIL)
cols=st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("#")
st.subheader("Experience & Qulifications")
st.write(' ✔️'"strong hands on python and mysql")
st.write(' ✔️'"Good understanding of statistical principles and their respective applications")
st.write(' ✔️'"Currently pursuing my BTech in cse from IPU UNIVERSITY DELHI ")

st.subheader("Hard Skills")
st.write(' ✔️'"Programming: Python (Scikit-learn, Pandas,numpy,web scraping)")
st.write(' ✔️'"Connecting and managing the database with python")
st.write("---")
st.subheader("Projects and Accomplishments")
for project,links in(PROJECTS.items()):
    st.write(f"[{project}]({links})")
