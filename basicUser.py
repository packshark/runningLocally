import streamlit as st
import pandas as pd
from io import StringIO

def app():
    st.title("Uploading Files")
    st.subheader("You have reached this page due to your current access permissions")
    st.markdown("---")

    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )

    # edit this later -- how do we want to design this?
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

    # later want to pass this to powerBI