import streamlit as st
import joblib 
clf=joblib.load('heart_disease.joblib')
st.title('HEART DISEASE PREDICTION')
a=st.number_input("Enter AGE")
cigs=st.number_input("Enter Cigs per day ")
ch=st.number_input("Enter total cholestrol ")
bp=st.number_input("Enter sysBP")
diabp=st.number_input("Enter diaBP")
bmi=st.number_input("Enter BMI")
hr=st.number_input("Enter heartRate")
gl=st.number_input("Enter glucose")
if st.button('PREDICT'):
    prediction=clf.predict([[a,cigs,ch,bp,diabp,bmi,hr,gl]])
    if prediction=='Y':
        st.text("CAN GET HEART DISEASE")
    else:
        st.text("CANNOT GET HEART DISEASE")
