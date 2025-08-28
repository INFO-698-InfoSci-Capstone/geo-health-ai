import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import json
from urllib.request import urlopen
import plotly.graph_objects as go
import urllib.request
import plotly.express as px

Unioned_Data_By_Race = pd.read_csv('../data/Unioned_Data_By_Race.csv')

## info for heatmap generation


CountyFIPSCode = {'CountyName' : ['Apache','Cochise','Coconino','Gila','Graham','Greenlee','La Paz','Maricopa','Mohave','Navajo','Pima','Pinal','Santa Cruz','Yavapai','Yuma'], 'FIPS_Code' : ['04001','04003','04005','04007','04009','04011','04012','04013','04015','04017','04019','04021','04023','04025','04027']}
CountyFIPSCode = pd.DataFrame(data = CountyFIPSCode)

Unioned_Data_FIPS = pd.merge(Unioned_Data_By_Race, CountyFIPSCode, on = 'CountyName', how = 'left')

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties_geojson = json.load(response)
mycustomdata = np.stack((Unioned_Data_FIPS['CountyName'], Unioned_Data_FIPS['%WhiteDiabetes'], Unioned_Data_FIPS['%BlackDiabetes']))



fig1 = px.choropleth(Unioned_Data_FIPS, geojson = counties_geojson,
                    locations = 'FIPS_Code', color='%BlackDiabetes',
                    color_continuous_scale = "Viridis",scope = "usa",
                    animation_frame = 'year',
                    title = 'Arizona County Heatmap Black Diabetes',
                    labels = {'%BlackDiabetes':'Diabetes<br>Percent'},
                    range_color = [10,25],
                    hover_data = ["CountyName"],
                    width = 900,
                    height = 350)

fig1.update_geos(center = {"lat": 34.0489,"lon": -111.0937},
                 projection_scale = 4,
                 scope = "usa")
fig1["layout"].pop("updatemenus") 

fig1.show()