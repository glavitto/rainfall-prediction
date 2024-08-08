import streamlit as st
import pickle
from PIL import Image
import pandas as pd
st.write("""
# RAINFALL PRIDICTION APP
    
this app will predict rainfall in Australia
""")
st.sidebar.header('User Input')

def main():
    
    image=Image.open('D:\luminar\project\pic.jpg')
    st.image(image,width=500)
    
    
    model=pickle.load(open('D:\luminar\project\model.pkl','rb'))
    scaler=pickle.load(open('D:\luminar\project\scaler.pkl','rb'))
    #
    #
    #
    wd= ["N", "NNE", "NE", "ENE","E", "ESE", "SE", "SSE","S", "SSW", "SW", "WSW","W", "WNW", "NW", "NNW"]
    MinTemp=st.sidebar.slider('Minimum Temprature in degrees Celsius',-5,50)
    MaxTemp=st.sidebar.slider('Maximum Temprature in degrees Celsius',-5,50)
    

    WindGustDir=st.sidebar.selectbox('Select direction of the strongest wind',wd)
    if WindGustDir=='W':
        WindGustDir=0
    elif WindGustDir=='WNW':
        WindGustDir=1
    elif WindGustDir=='WSW':
        WindGustDir=2
    elif WindGustDir=='NE':
        WindGustDir=3
    elif WindGustDir=='NNW':
        WindGustDir=4
    elif WindGustDir=='N':
        WindGustDir=5
    elif WindGustDir=='NNE':
        WindGustDir=6
    elif WindGustDir=='SW':
        WindGustDir=7
    elif WindGustDir=='ENE':
        WindGustDir=8
    elif WindGustDir=='SSE':
        WindGustDir=9
    elif WindGustDir=='s':
        WindGustDir=10
    elif WindGustDir=='NW':
        WindGustDir=11
    elif WindGustDir=='SE':
        WindGustDir=12
    elif WindGustDir=='ESE':
        WindGustDir=13
    elif WindGustDir=='E':
        WindGustDir=14
    else:
        WindGustDir=14
    Rainfall=st.sidebar.slider('rainfall recorded for the day in millimeters',0,375)
    WindGustSpeed=st.sidebar.slider('speed of the strongest wind gust in KM/H',0,135)

    WindDir9am=st.sidebar.selectbox("Select direction of the wind at 9 AM", wd)
    if WindDir9am=='W':
        WindDir9am=0
    elif WindDir9am=='WNW':
        WindDir9am=1
    elif WindDir9am=='WSW':
        WindDir9am=2
    elif WindDir9am=='NE':
        WindDir9am=3
    elif WindDir9am=='NNW':
        WindDir9am=4
    elif WindDir9am=='N':
        WindDir9am=5
    elif WindDir9am=='NNE':
        WindDir9am=6
    elif WindDir9am=='SW':
        WindDir9am=7
    elif WindDir9am=='ENE':
        WindDir9am=8
    elif WindDir9am=='SSE':
        WindDir9am=9
    elif WindDir9am=='s':
        WindDir9am=10
    elif WindDir9am=='NW':
        WindDir9am=11
    elif WindDir9am=='SE':
        WindDir9am=12
    elif WindDir9am=='ESE':
        WindDir9am=13
    elif WindDir9am=='E':
        WindDir9am=14
    else:
        WindDir9am=14

    WindDir3pm=st.sidebar.selectbox("Select direction of the wind at 3 PM", wd)
    if WindDir3pm=='W':
        WindDir3pm=0
    elif WindDir3pm=='WNW':
        WindDir3pm=1
    elif WindDir3pm=='WSW':
        WindDir3pm=2
    elif WindDir3pm=='NE':
        WindDir3pm=3
    elif WindDir3pm=='NNW':
        WindDir3pm=4
    elif WindDir3pm=='N':
        WindDir3pm=5
    elif WindDir3pm=='NNE':
        WindDir3pm=6
    elif WindDir3pm=='SW':
        WindDir3pm=7
    elif WindDir3pm=='ENE':
        WindDir3pm=8
    elif WindDir3pm=='SSE':
        WindDir3pm=9
    elif WindDir3pm=='s':
        WindDir3pm=10
    elif WindDir3pm=='NW':
        WindDir3pm=11
    elif WindDir3pm=='SE':
        WindDir3pm=12
    elif WindDir3pm=='ESE':
        WindDir3pm=13
    elif WindDir3pm=='E':
        WindDir3pm=14
    else:
        WindDir3pm=14

    WindSpeed9am=st.sidebar.slider('Wind speed at 9am in KM/H',0,135)
    WindSpeed3pm=st.sidebar.slider('Wind speed at 3pm in KM/H',0,135)
    Humidity9am=st.sidebar.slider('Humidity percentage at 9 AM',0,100)
    Humidity3pm=st.sidebar.slider('Humidity percentage at 3 PM',0,100)
    Pressure9am=st.sidebar.slider('Atmospheric pressure at 9 AM in hPa',970,1041)
    Pressure3pm=st.sidebar.slider('Atmospheric pressure at 3 PM in hPa',970,1041)
    Temp9am=st.sidebar.slider('Temprature at 9 AM',-5,50)
    Temp3pm=st.sidebar.slider('Temprature at 3 PM',-5,50)

    RainToday=st.sidebar.radio("Is it raining today?", ("Yes", "No"))
    if RainToday=='Yes':
        RainToday=1
    else:
        RainToday=0
    #
    #
    pred=st.sidebar.button('Predict')
    if pred:
        prediction=model.predict(scaler.transform([[float(MinTemp),float(MaxTemp),float(Rainfall),int(WindGustDir),
                                                    float(WindGustSpeed),int(WindDir9am),int(WindDir3pm),
                                                    float(WindSpeed9am),float(WindSpeed3pm),float(Humidity9am),
                                                    float(Humidity3pm),float(Pressure9am),float(Pressure3pm),
                                                    float(Temp9am),float(Temp3pm),int(RainToday)]]))
        if prediction==0:
            st.sidebar.write('Rainy day ahead')
        else:
            st.sidebar.write('Dry day ahead')


main()