import pandas as pd
import json
from urllib.request import urlopen
import plotly.express as px

Unioned_Data_By_Race = pd.read_csv('data/Unioned_Data_By_Race.csv')

## info for heatmap generation


CountyFIPSCode = {'CountyName' : ['Apache','Cochise','Coconino','Gila','Graham','Greenlee','La Paz','Maricopa','Mohave','Navajo','Pima','Pinal','Santa Cruz','Yavapai','Yuma'], 'FIPS_Code' : ['04001','04003','04005','04007','04009','04011','04012','04013','04015','04017','04019','04021','04023','04025','04027']}
CountyFIPSCode = pd.DataFrame(data = CountyFIPSCode)

Unioned_Data_FIPS = pd.merge(Unioned_Data_By_Race, CountyFIPSCode, on = 'CountyName', how = 'left')

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties_geojson = json.load(response)


fig1 = px.choropleth(Unioned_Data_FIPS, geojson = counties_geojson,
                    locations = 'FIPS_Code', color='%OMultirObesity',
                    color_continuous_scale = "Viridis",scope = "usa",
                    animation_frame = 'year',
                    title = 'Arizona County Heatmap Other Obesity',
                    labels = {'%OMultirObesity':'Obesity<br>Percent'},
                    range_color = [20,50],
                    hover_data = ["CountyName"])

fig1.update_geos(center = {"lat": 34.0489,"lon": -111.0937},
                 projection_scale = 4,
                 scope = "usa")

fig1.show()