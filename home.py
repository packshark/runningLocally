import streamlit as st

def app():
    if st.session_state.username == "phone" and st.session_state.password == "hellokitty":
        st.title("Hello " + st.session_state.username)
        st.write("You have access to the Customer Portal and the Operations Portal.")

    elif st.session_state.username == "laptop" and st.session_state.password == "chamberofsecrets":
        st.title("Hello " + st.session_state.username)
        st.write("You have access to the Customer Portal.")

    else:
        st.title("Welcome")
