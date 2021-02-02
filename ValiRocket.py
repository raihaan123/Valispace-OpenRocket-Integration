import streamlit as st
import streamlit.components.v1 as components #For components.HTML
import valispace
import time
import pandas as pd

st.beta_set_page_config(page_title="ValiRocket", page_icon="https://iclrocketry.valispace.com/assets/img/logo/icon.png")

"""
# ValiRocket.
Imperial College Rocketry
"""
st.sidebar.write("Designed by ya boi Raihaan")

user = st.sidebar.text_input("Username", '')
passwd = st.sidebar.text_input("Password",type="password")
if passwd:
    with st.spinner("Logging in..."):
        try:
            vs = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
            st.success("Success!")
        except:
            st.error('Invalid credentials')
        

option = st.selectbox('What u wanna do m8?',
                        ('Track changes','First push'))

st.write("You picked " + option) 