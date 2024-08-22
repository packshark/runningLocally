import streamlit as st
import admin, cust, basicUser

def app():
    st.title("Welcome to the Packing Portal")
    st.write("Please log in to continue")

    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'loggedOut' not in st.session_state:
        st.session_state.loggedOut = True

    if st.session_state.loggedOut:
        with st.form("login_form"):
            username = st.text_input("Username", key="login_username")  # Unique key
            password = st.text_input("Password", type="password", key="login_password")  # Unique key
            submit_button = st.form_submit_button('Submit')  # Unique key

            if submit_button:
                if username == "phone" and password == "hellokitty":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    admin.app()

                elif username == "laptop" and password == "chamberofsecrets":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    cust.app()

                elif username == "hehe" and password == "helloworld":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    basicUser.app()

                else:
                    st.error("Incorrect username or password")
    else:
        st.success(f"Logged in as {st.session_state.username}")
        if st.session_state.username == "phone":
            admin.app()
        elif st.session_state.username == "laptop":
            cust.app()
        elif st.session_state.username == "hehe":
            basicUser.app()
        else:
            st.session_state.loggedOut = True
            st.experimental_rerun()  # Rerun to display the login form again
