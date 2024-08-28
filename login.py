import streamlit as st

import home, basicUser, logout

if 'password' not in st.session_state:
    st.session_state.password = ""


def app():

    st.title("Hello")
    if st.session_state.loggedOut:
        with st.form("login_form"):
            username = st.text_input("Username", key="login_username")  # Unique key
            password = st.text_input("Password", type="password", key="login_password")  # Unique key
            submit_button = st.form_submit_button('Submit')  

            if submit_button:
                if username == "phone" and password == "hellokitty":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    st.session_state.user_type = "Admin"
                    # bug - st.experimental_rerun()  # Rerun to avoid executing the rest of the code
                    st.success("You are logged in as " + st.session_state.user_type)
                    st.write("Please click on Home in the navigation to refresh your access.")

                elif username == "laptop" and password == "chamberofsecrets":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    st.session_state.user_type = "Customer"
                    st.success("You are logged in as " + st.session_state.user_type)
                    st.write("Please click on Home in the navigation to refresh your access.")

                elif username == "hehe" and password == "helloworld":
                    st.session_state.username = username
                    st.session_state.loggedOut = False
                    st.session_state.user_type = "Basic"
                    st.success("You are logged in as " + st.session_state.user_type)
                    st.write("Please click on Home in the navigation to refresh your access.")

                else:
                    st.error("Incorrect username or password")
    else:
        
        if st.session_state.loggedOut == False:
            home.app()
    
        else:
            st.session_state.loggedOut = True
            app()
