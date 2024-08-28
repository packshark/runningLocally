import streamlit as st

def app():
    
    if st.session_state.user_type == "Admin":
        st.title(f"Welcome home {st.session_state.username}!")
        st.info(f"You are logged in as {st.session_state.user_type}.")
        st.write("You have access to the Customer Portal and the Operations Portal.")

    elif st.session_state.user_type == "Customer":
         st.title(f"Welcome home {st.session_state.username}!")
         st.info(f"You are logged in as {st.session_state.user_type}.")
         st.write("You have access to the Customer Portal.")

    elif st.session_state.user_type == "Basic":
         st.title(f"Welcome home {st.session_state.username}!")
         st.info(f"You are logged in as {st.session_state.user_type}.")
         st.write("You can upload files and view the stats. If you want portal access, contact your admin.")
         # or should we have you you have not used your devices for the web yet

    else:
        st.title("Welcome. You are not logged in.")
        st.info("If you clicked on 'Logout' but are still seeing this page, you need to click 'Logout' one more time.")
