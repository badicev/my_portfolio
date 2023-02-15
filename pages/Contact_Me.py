import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form"):
    user_email = st.text_input("Your email adress:")
    text = st.text_area("Your message:")
    #message = text + "\n" + user_email

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{text}"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("You mail was sent succesfully.")