import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def main():
    """Hepatitis Prediction App"""
    st.title("Hepatitis Prediction App")

    menu = ["Home", "Login", "SignUp"]
    submenu = ["Visualization", "Prediction"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.text("What is Hepatitis?")
    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type= 'password')
        if st.sidebar.checkbox("Login"):
            if password == "12345":
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity", submenu)
                if activity == "Visualize":
                    st.subheader("Data Visualization")
                elif activity == "Prediction":
                    st.subheader("Predictive Analytics")
                    
            else:
                st.warning("Incorrect Username/Password")



if __name__ == '__main__':
    main()
    
    
    
