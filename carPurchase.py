import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model/car_purchase.joblib")

st.markdown("<h1 style='text-align: center; color: #008BFF;'>Car purchase🚗</h1>", unsafe_allow_html=True)
st.write("---")
col1, col2, col3 = st.columns(3)
sex = col1.radio("Sex", ["Male", "Female"])
age = col2.number_input("Age", 0, 100)
monthly_salary = col3.number_input("Monthly Salary in USD", 0.0)
st.write("---")

df = pd.DataFrame({
    "Gender": [1 if sex=="Male" else 0],
    "Age": [age],
    "AnnualSalary": [monthly_salary*12]
})
res = model.predict(df)[0]
if res==1:
    st.write("## ✅You can purchase!!")
else:
    st.write("## ❌You Can't purchase")
