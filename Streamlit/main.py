import streamlit as st

def fuc1():
  a = st.number_input('Pick a number',key=1)
  b= st.number_input('Pick a number', 0, 10,key=2)
  return a+b

def fuc2():
  a = st.number_input('Pick a number', 0, 10,key=3)
  b= st.number_input('Pick a number', 0, 10,key=4)
  st.balloons()
  return a-b

with st.sidebar:
  value = st.radio('Select one:', ["add", "sub"])

if value == "add":
    result = fuc1()
    st.header(result)

else:
    result = fuc2()
    st.header(result)
