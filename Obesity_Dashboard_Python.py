import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import json
from urllib.request import urlopen
import plotly.graph_objects as go
import urllib.request
import plotly.express as px

Unioned_Data_By_Race = pd.read_csv('data/Unioned_Data_By_Race.csv')

## info for heatmap generation


CountyFIPSCode = {'CountyName' : ['Apache','Cochise','Coconino','Gila','Graham','Greenlee','La Paz','Maricopa','Mohave','Navajo','Pima','Pinal','Santa Cruz','Yavapai','Yuma'], 'FIPS_Code' : ['04001','04003','04005','04007','04009','04011','04012','04013','04015','04017','04019','04021','04023','04025','04027']}
CountyFIPSCode = pd.DataFrame(data = CountyFIPSCode)

Unioned_Data_FIPS = pd.merge(Unioned_Data_By_Race, CountyFIPSCode, on = 'CountyName', how = 'left')

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties_geojson = json.load(response)
mycustomdata = np.stack((Unioned_Data_FIPS['CountyName'], Unioned_Data_FIPS['%WhiteDiabetes'], Unioned_Data_FIPS['%BlackDiabetes']))



fig1 = px.choropleth(Unioned_Data_FIPS, geojson = counties_geojson,
                    locations = 'FIPS_Code', color='%WhiteObesity',
                    color_continuous_scale = "Viridis",scope = "usa",
                    animation_frame = 'year',
                    title = 'Arizona County Heatmap Obesity<br><sub>Select a racial group from the dropdown</sub>',
                    labels = {'%WhiteObesity':'Obesity<br>Percent'},
                    range_color = [20,50],
                    hover_data = ["CountyName"],
                    width = 900,
                    height = 350)

fig1.update_geos(center = {"lat": 34.0489,"lon": -111.0937},
                 projection_scale = 4,
                 scope = "usa")
fig1["layout"].pop("updatemenus") 
box7 = dict(method = 'update', label = 'White Obesity', args = [{'z': [Unioned_Data_FIPS['%WhiteObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}'}])
box8 = dict(method = 'update', label = 'Black Obesity', args = [{'z': [Unioned_Data_FIPS['%BlackObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}%'}])
box9 = dict(method = 'update', label = 'Asian Obesity', args = [{'z': [Unioned_Data_FIPS['%AsianObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}'}])
box10 = dict(method = 'update', label = 'Native Hawaiian or Pacific Islander Obesity', args = [{'z': [Unioned_Data_FIPS['%NHOPIObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}'}])
box11 = dict(method = 'update', label = 'American Indian and Alaska Native Obesity', args = [{'z': [Unioned_Data_FIPS['%AIANObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}'}])
box12 = dict(method = 'update', label = 'Other Obesity', args = [{'z': [Unioned_Data_FIPS['%OMultirObesity']],'hovertemplate': 'County: %{customdata[0]}<br> Obesity: %{z}'}])

fig1.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=[box7, box8, box9, box10, box11, box12],
            type="dropdown",
            direction="down",
            showactive=True,
            x=0.001, 
            xanchor="left",
            y=1,
            yanchor="top",
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            font=dict(size=12),
            pad={"r": 10, "t": 10},
        )
    ],
    coloraxis_colorbar=dict(
        title='Diabetes Percent'
    )
)


fig1.show()