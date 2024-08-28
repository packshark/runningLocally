import streamlit as st

def app():
    st.title("Operations Portal")
    st.info(f"You are logged in as {st.session_state.user_type}.")
