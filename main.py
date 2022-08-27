import streamlit as st
import pickle

st.set_page_config(page_title="Body fat App",layout="centered")
st.title("Body Fat Prediction")

pickle_in = open('Bodyfat.pickle', 'rb')
lr = pickle.load(pickle_in)

number1 = st.number_input('	Abdomen', key='1')
number2 = st.number_input('Chest', key='2')
number3 = st.number_input('Hip', key='3')
number4 = st.number_input('Weight', key='4')
number5 = st.number_input('Thigh', key='5')


if st.button("Predict"):
    pred = str(lr.predict([[number1, number2, number3, number4, number5]]))
    st.success("Body Fat prediction : " + pred)
