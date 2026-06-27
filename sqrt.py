import streamlit as st
import math

st.title("Square Root Calculator")

x = st.number_input("Enter a number", min_value=0)

if st.button("Calculate"):
    y = math.sqrt(x)
    st.write("Square root =", y)
