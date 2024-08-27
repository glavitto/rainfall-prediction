import streamlit as st
import pickle
from PIL import Image

st.write("""
# RAINFALL PREDICTION APP

This app will predict rainfall in Australia.
""")

st.sidebar.header('User Input')

def main():
    # Load image
    try:
        image = Image.open(r'D:\luminar\rainfall prediction\pic.jpg')
        st.image(image, width=500)
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")
        return
    
    # Load model and scaler
    try:
        model = pickle.load(open(r'D:\luminar\rainfall prediction\model.pkl', 'rb'))
        scaler = pickle.load(open(r'D:\luminar\rainfall prediction\scaler.pkl', 'rb'))
    except FileNotFoundError as e:
        st.error(f"File not found: {e}")
        return
    except Exception as e:
        st.error(f"Error loading model or scaler: {e}")
        return
    
    # Define options
    wd = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    loc = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree', 'NorahHead',
           'NorfolkIsland', 'Richmond', 'Sydney', 'SydneyAirport', 'WaggaWagga',
           'Williamtown', 'Wollongong', 'Canberra', 'Tuggeranong', 'Ballarat', 'Bendigo',
           'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura', 'Nhil', 'Portland',
           'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns', 'GoldCoast', 'Townsville',
           'Adelaide', 'MountGambier', 'Nuriootpa', 'Woomera', 'Witchcliffe',
           'PearceRAAF', 'PerthAirport', 'Perth', 'Walpole', 'Hobart', 'Launceston',
           'AliceSprings', 'Darwin', 'Katherine', 'Uluru']
    
     # User inputs
    Location = st.sidebar.selectbox('Location', loc, index=0)
    MinTemp = st.sidebar.slider('Minimum Temperature in degrees Celsius', -5, 50, value=16)
    MaxTemp = st.sidebar.slider('Maximum Temperature in degrees Celsius', -5, 50, value=22)
    WindGustDir = st.sidebar.selectbox('Select direction of the strongest wind', wd, index=1)
    Rainfall = st.sidebar.slider('Rainfall recorded for the day in millimeters', 0, 375, value=2)
    WindGustSpeed = st.sidebar.slider('Speed of the strongest wind gust in KM/H', 0, 135, value=31)
    WindDir9am = st.sidebar.selectbox("Select direction of the wind at 9 AM", wd, index=2)
    WindDir3pm = st.sidebar.selectbox("Select direction of the wind at 3 PM", wd, index=3)
    WindSpeed9am = st.sidebar.slider('Wind speed at 9 AM in KM/H', 0, 135, value=15)
    WindSpeed3pm = st.sidebar.slider('Wind speed at 3 PM in KM/H', 0, 135, value=13)
    Humidity9am = st.sidebar.slider('Humidity percentage at 9 AM', 0, 100, value=89)
    Humidity3pm = st.sidebar.slider('Humidity percentage at 3 PM', 0, 100, value=91)
    Pressure9am = st.sidebar.slider('Atmospheric pressure at 9 AM in hPa', 970, 1041, value=1011)
    Pressure3pm = st.sidebar.slider('Atmospheric pressure at 3 PM in hPa', 970, 1041, value=1004)
    Temp9am = st.sidebar.slider('Temperature at 9 AM', -5, 50, value=16)
    Temp3pm = st.sidebar.slider('Temperature at 3 PM', -5, 50, value=17)
    RainToday = st.sidebar.radio("Is it raining today?", ("Yes", "No"))
    RainToday = 1 if RainToday == 'Yes' else 0
    
    # Prediction
    pred = st.sidebar.button('Predict')
    if pred:
        try:
            prediction = model.predict(scaler.transform([[loc.index(Location), MinTemp, MaxTemp, Rainfall, wd.index(WindGustDir),
                                                          WindGustSpeed, wd.index(WindDir9am), wd.index(WindDir3pm),
                                                          WindSpeed9am, WindSpeed3pm, Humidity9am,
                                                          Humidity3pm, Pressure9am, Pressure3pm,
                                                          Temp9am, Temp3pm, RainToday]]))
            if prediction == 0:
                st.write('Dry day ahead')
            else:
                st.write('Rainy day ahead')
        except Exception as e:
            st.error(f"Error making prediction: {e}")

main()
