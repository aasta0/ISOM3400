import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Retail Business Dashboard")

st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")

sales_target = st.number_input("Enter Monthly Sales Target (in USD): ", value = 0)
st.write(f"The monthly sales target (in USD) is {sales_target}.")
