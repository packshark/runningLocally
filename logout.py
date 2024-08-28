import streamlit as st
import home

def app():
    st.session_state.loggedOut = True
    st.session_state.username = ""
    st.session_state.user_type = ""
    home.app()
