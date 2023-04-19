import streamlit as st
a=st.number_input(int(input("Enter 1st number:")))
b=st.number_input(int(input("Enter 2nd number:")))
c=st.number_input(int(input("Enter 3rd number:")))
if (a>=b) and (a>=c):
  m=a
elif (b>=a) and (b>=c):
  m=b
else (c>=a) and(c>=b):
  m=c
st.write("Largest of 3 numbers:",m)
