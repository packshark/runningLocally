import streamlit as st
from streamlit_option_menu import option_menu
import about, login, admin, basicUser, cust, home

page_title = "Portal"

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Portal',
                options=['Home', 'About', 'Account'],
                icons=['house-fill', 'chat-fill', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
                key="main_menu"  # Add a unique key here
            )

        if app == 'Home':
            home.app()
        elif app == 'About':        
            about.app()
        elif app == 'Account':
            login.app()
        elif app == 'Basic':
            basicUser.app()
        elif app == 'Admin':
            admin.app()
        elif app == 'Cust':
            cust.app()

# Create an instance of the MultiApp class
app = MultiApp()

# Add all your applications here
app.add_app('Home', home.app)
app.add_app('About', about.app)
app.add_app('Account', login.app)
app.add_app('Basic', basicUser.app)
app.add_app('Customer', cust.app)
app.add_app('Admin', admin.app)

# Run the main app
app.run()