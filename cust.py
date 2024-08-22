import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import os
import pathlib

def app():
    st.write('Customer Use')

# Get the current path of the main file
current_path = pathlib.Path(__file__)

# Print the current path to the Streamlit app
st.write(f"Current path of the main file: {current_path}")

st.title("Customer Portal")
st.markdown("Customer Portal")
st.sidebar.header("Customer Portal")
st.sidebar.header("Operations Portal")

# table Rithik shared -- though we might not need this once we have the Power BI table and can do everything through there
data = pd.read_csv("fake_dns_log.csv")
st.dataframe(data)

# Power BI table
# do we want to upload and reflect anything?
components.iframe("https://app.powerbi.com/reportEmbed?reportId=c2d0d27d-4aab-4cb8-94ab-f793dade383c&autoAuth=true&ctid=e741d71c-c6b6-47b0-803c-0f3b32b07556", height =600, width = 800)