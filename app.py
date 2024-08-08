import streamlit as st
import pickle
from PIL import Image
import pandas as pd

st.write("""
# RAINFALL PREDICTION APP

This app will predict rainfall in Australia.
""")

st.sidebar.header('User Input')

def main():
    image = Image.open('pic.jpg')
    st.image(image, width=500)
    
    
    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    wd = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    
    MinTemp = st.sidebar.slider('Minimum Temperature in degrees Celsius', -5, 50)
    MaxTemp = st.sidebar.slider('Maximum Temperature in degrees Celsius', -5, 50)
    WindGustDir = st.sidebar.selectbox('Select direction of the strongest wind', wd)
    WindGustDir = wd.index(WindGustDir)
    Rainfall = st.sidebar.slider('Rainfall recorded for the day in millimeters', 0, 375)
    WindGustSpeed = st.sidebar.slider('Speed of the strongest wind gust in KM/H', 0, 135)
    
    WindDir9am = st.sidebar.selectbox("Select direction of the wind at 9 AM", wd)
    WindDir9am = wd.index(WindDir9am)
    WindDir3pm = st.sidebar.selectbox("Select direction of the wind at 3 PM", wd)
    WindDir3pm = wd.index(WindDir3pm)
    
    WindSpeed9am = st.sidebar.slider('Wind speed at 9 AM in KM/H', 0, 135)
    WindSpeed3pm = st.sidebar.slider('Wind speed at 3 PM in KM/H', 0, 135)
    Humidity9am = st.sidebar.slider('Humidity percentage at 9 AM', 0, 100)
    Humidity3pm = st.sidebar.slider('Humidity percentage at 3 PM', 0, 100)
    Pressure9am = st.sidebar.slider('Atmospheric pressure at 9 AM in hPa', 970, 1041)
    Pressure3pm = st.sidebar.slider('Atmospheric pressure at 3 PM in hPa', 970, 1041)
    Temp9am = st.sidebar.slider('Temperature at 9 AM', -5, 50)
    Temp3pm = st.sidebar.slider('Temperature at 3 PM', -5, 50)

    RainToday = st.sidebar.radio("Is it raining today?", ("Yes", "No"))
    RainToday = 1 if RainToday == 'Yes' else 0
    
    pred = st.sidebar.button('Predict')
    if pred:
        prediction = model.predict(scaler.transform([[MinTemp, MaxTemp, Rainfall, WindGustDir,
                                                      WindGustSpeed, WindDir9am, WindDir3pm,
                                                      WindSpeed9am, WindSpeed3pm, Humidity9am,
                                                      Humidity3pm, Pressure9am, Pressure3pm,
                                                      Temp9am, Temp3pm, RainToday]]))
        if prediction == 0:
            st.write('Dry day ahead')
        else:
            st.write('Rainy day ahead')


main()
