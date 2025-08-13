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
mycustomdata = np.stack((Unioned_Data_FIPS['CountyName'],Unioned_Data_FIPS['%WhiteDiabetes'],Unioned_Data_FIPS['%BlackDiabetes']))

fig2 = px.choropleth(Unioned_Data_FIPS, geojson = counties_geojson,
                    locations = 'FIPS_Code', color = '%WhiteDiabetes',
                    color_continuous_scale = "Viridis",scope = "usa",
                    animation_frame = 'year',
                    title = 'Arizona County Heatmap for Diabetes Rates',
                    labels = {'%WhiteDiabetes':'Diabetes Percent'},
                    range_color = [10,25],
                    hover_data = ["CountyName"])

fig2.update_geos(center = {"lat": 34.0489,"lon": -111.0937},
                 projection_scale = 4,
                 scope = "usa")
fig2["layout"].pop("updatemenus") 
box1 = dict(method = 'update', label = 'White Diabetes', args = [{'z': [Unioned_Data_FIPS['%WhiteDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])
box2 = dict(method = 'update', label = 'Black Diabetes', args = [{'z': [Unioned_Data_FIPS['%BlackDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])
box3 = dict(method = 'update', label = 'Asian Diabetes', args = [{'z': [Unioned_Data_FIPS['%AsianDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])
box4 = dict(method = 'update', label = 'Native Hawaiian and Pacific Islander Diabetes', args = [{'z': [Unioned_Data_FIPS['%NHOPIDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])
box5 = dict(method = 'update', label = 'American Indian and Alaska Native Diabetes', args = [{'z': [Unioned_Data_FIPS['%AIANDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])
box6 = dict(method = 'update', label = 'Other Diabetes', args = [{'z': [Unioned_Data_FIPS['%OMultirDiabetes']],'hovertemplate': 'County: %{customdata[0]}<br> Diabetes: %{z}'}])


fig2.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=[box1,box2,box3,box4,box5,box6],
            type = "dropdown",
            direction="down",
            showactive=False,
            x=0.001,
            xanchor="left",
            y=1.2,
            yanchor="top"
        )
    ]
)

fig2.show()