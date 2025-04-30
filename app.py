import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Grafico de vehiculos')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

dis_button = st.button('Construir grafico dispersion') # crear un botón
        
if dis_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un dispersion
            fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

