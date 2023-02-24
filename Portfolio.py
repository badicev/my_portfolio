import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 2, 0.25])

df = pd.read_csv("data.csv", sep=";")



with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Başak Dilara Çevik")
    content1 = """After graduating from the department of economics,
      I started to pursue my master's degree in economics and had the opportunity to develop
       myself in the research area.
        Currently, I am conducting a thesis study to accelerate the adoption of electric vehicles
         in Turkey within the scope of sustainability. In this process,
          I significantly improved my knowledge of game development with Unity, project management, 
          and game art with the help of Oyun ve Uygulama Akademisi. 
          Besides all these, I have been actively developing myself in the fields of data science and machine learning 
          for the last three years, participating in various events and communities. :)"""
    st.info(content1)

content2 = """This is my portfolio. You can navigate between the bars to see my projects."""
st.subheader(content2)

tab1, tab2, tab3, tab4, tab5, tab6,\
tab7, tab8, tab9, tab10, \
tab11, tab12, \
tab13, tab14, tab15 = st.tabs(["To-Do App", "Portfolio", "PDF Generation", "Excel Invoices to PDF",
                                  "Email News", "Weather API", "Book Sentiment Analysis",
                                  "Email Webcam Object Detection", "Web Scraping Musical Events",
                                  "Hotel Booking", "Super Mario Game Code Inspection",
                                  "Student Management System", "Chatbot", "Astronomy Image of the Day"])

#if you prefer columnwise rather than tabwise
# for index, row in df.iterrows():
#     st.header(row["title"])
#     st.write(row["description"])
#     st.image("images/" + row["image"])
#     st.write("[Source Code](https://badice.com.tr)")

with tab1:
   st.header("To-Do App")
   st.write(df["description"][0])
   st.image("images/1.png", width=500)
   st.write(f"[Source Code]({df['url'][0]})")


with tab2:
   st.header("Portfolio")
   st.write(df["description"][1])
   st.image("images/2.png", width=500)
   st.write(f"[Source Code]({df['url'][1]})")

with tab3:
   st.header("Excel Invoices to PDF")
   st.write(df["description"][2])
   st.image("images/3.png", width=500)
   st.write(f"[Source Code]({df['url'][2]})")

with tab4:
    st.header("")
    st.write(df["description"][3])
    st.image("images/4.png", width=500)
    st.write(f"[Source Code]({df['url'][3]})")

with tab5:
    st.header("")
    st.write(df["description"][4])
    st.image("images/5.png", width=500)
    st.write(f"[Source Code]({df['url'][4]})")

with tab6:
    st.header("")
    st.write(df["description"][5])
    st.image("images/6.png", width=500)
    st.write(f"[Source Code]({df['url'][5]})")

with tab7:
    st.header("")
    st.write(df["description"][6])
    st.image("images/7.png", width=500)
    st.write(f"[Source Code]({df['url'][6]})")

with tab8:
    st.header("")
    st.write(df["description"][7])
    st.image("images/8.png", width=500)
    st.write(f"[Source Code]({df['url'][7]})")

with tab9:
    st.header("")
    st.write(df["description"][8])
    st.image("images/9.png", width=500)
    st.write(f"[Source Code]({df['url'][8]})")

with tab10:
    st.header("")
    st.write(df["description"][9])
    st.image("images/10.png", width=500)
    st.write(f"[Source Code]({df['url'][9]})")

with tab11:
    st.header("")
    st.write(df["description"][10])
    st.image("images/11.png", width=500)
    st.write(f"[Source Code]({df['url'][10]})")

with tab12:
    st.header("")
    st.write(df["description"][11])
    st.image("images/12.png", width=500)
    st.write(f"[Source Code]({df['url'][11]})")

with tab13:
    st.header("")
    st.write(df["description"][12])
    st.image("images/13.png", width=500)
    st.write(f"[Source Code]({df['url'][12]})")
    
with tab14:
    st.header("")
    st.write(df["description"][13])
    st.image("images/14.png", width=500)
    st.write(f"[Streamlit Website]({df['url'][13]})")

with tab15:
    st.header("")
    st.write(df["description"][17])
    st.image("images/17.png", width=500)
    st.write(f"[Streamlit Website]({df['url'][17]})")
