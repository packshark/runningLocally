import streamlit as st
from streamlit_option_menu import option_menu
import login, basicUser, customer_portal, home, operations_portal, logout

page_title = "Portal"

if 'loggedOut' not in st.session_state:
    st.session_state.loggedOut = True
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'user_type' not in st.session_state:
    st.session_state.user_type = ""

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
         # Initialize session state if not already done

        with st.sidebar:
            # Define different menus for different user types
            if st.session_state.user_type == "Admin":
                options = ['Home', 'Operations Portal','Customer Portal', 'Logout']
                icons = ['house-fill', 'shield-fill', 'person-circle','power']
            elif st.session_state.user_type == "Customer":
                options = ['Home', 'Customer Portal', 'Logout']
                icons = ['house-fill', 'person-circle', 'power']
            elif st.session_state.user_type == "Basic":
                options = ['Home', 'View Stats', 'Logout']
                icons = ['house-fill', 'person-circle', 'gear-fill']
            else:
                options = ['Home','Login']
                icons = ['house-fill']

            app_selection = option_menu(
                menu_title='Portal',
                options=options,
                icons=icons,
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
                key="main_menu"  
            )

        # if app_selection == 'Logout':
        #     st.session_state.loggedOut = True
        #     st.session_state.username = ""
        #     st.session_state.user_type = ""
        #     app_entry['title'] = "Home"
        #     app_entry["function"]()
        # else:
        #     # Map the selected menu option to the corresponding app function
        #     for app_entry in self.apps:
        #         if app_selection == app_entry["title"]:
        #             app_entry["function"]()
     
        # Map the selected menu option to the corresponding app function
        for app_entry in self.apps:
            if app_selection == app_entry["title"]:
                app_entry["function"]()

# Create an instance of the MultiApp class
app = MultiApp()

# Add all your applications here
app.add_app('Home', home.app)
app.add_app('Customer Portal', customer_portal.app)
app.add_app('Operations Portal', operations_portal.app)
app.add_app('Login', login.app)
app.add_app('Logout', logout.app)
app.add_app('View Stats', basicUser.app)

# Run the main app
app.run()
