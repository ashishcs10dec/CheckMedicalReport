import streamlit as st
import Gemini_Helper
import json

gender = st.sidebar.selectbox("Gender",("Male","Female"))

agelst = []
for i in range(1, 100):
    agelst.append(i)

#age = st.sidebar.selectbox("Age",("10","11","12","13","14","15",
 #                                 "16","17","18","19","20","21","22","23","24","25",
  #                                "26","27","28","29","30","31","32","33","34","35"))

age = st.sidebar.selectbox("Age",agelst)

st.header('Enter Your Medical Test with Value')
txt = st.text_area("")

if st.button("CHECK"):
    if txt:
        pass
        response = Gemini_Helper.generate_report_summary(gender, age, txt)
        df = json.loads(response)
        st.markdown(df[0]["RESULT"])
        #st.header(df[0]["RESULT"])



