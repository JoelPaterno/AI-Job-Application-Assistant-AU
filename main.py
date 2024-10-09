import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("AI Job Application Assistant AU")
st.write("Welcome to AI Job Application Assistant AU")

#Main Section 
st.file_uploader("Upload your resume", type=["pdf"])

left_column, right_column = st.columns([4, 1], vertical_alignment="center")

left_column.text_input("Find Jobs by Role", key="role") 
right_column.button("Find Jobs")



#Side Bar

if 'Roles' not in st.session_state:
    st.session_state.Roles = []

side_radio = st.sidebar.radio(
    "Role's to look for:", 
    (role for role in st.session_state.Roles)
)

side_new_role = st.sidebar.text_input("Enter new role: ", key="new_role")


def add_role():
    """
    Add a new role to the list of roles to look for. This function is
    called when the "Add new role" button is clicked in the sidebar.
    """
    if st.session_state.new_role:
        st.session_state.Roles.append(st.session_state.new_role)
        st.session_state.new_role = ""

side_button = st.sidebar.button("Add new role", on_click=add_role)