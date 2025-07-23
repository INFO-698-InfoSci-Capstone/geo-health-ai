
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

FARA = pd.read_csv('../data/FARA.csv')
AZ_FARA = FARA[FARA['State'] == 'Arizona']
AZ_FARA.head()
PCTDG = pd.read_csv('../data/PLACES.csv')
PCTDG = PCTDG.rename(columns = {'TractFIPS': 'TRACT'})
PCTDG.head()

#AL = pd.read_csv('data/addresses.csv', delimiter = ',')
#AL['BLOCK_GEOID'] = pd.to_numeric(AL['BLOCK_GEOID'], downcast = 'integer')
#AL['BLOCK_GEOID'] = AL['BLOCK_GEOID'].floordiv(10000)
#AL = AL.drop(['STATE','COUNTY','BLOCK','TRACT'], axis = 1)
#AL = AL.rename(columns = {'BLOCK_GEOID': 'CensusTract'})
#AL['CensusTract'] = AL['CensusTract'].astype(str)
#AL['CensusTract'] = AL['CensusTract'].str.slice(start = 4)
#AL_group = AL.groupby(['CensusTract']).sum()
##AL_group

#AL

#AZ_FARA['CensusTract'] = AZ_FARA['CensusTract'].astype(str)
#AZ_FARA['CensusTract'] = AZ_FARA['CensusTract'].str.slice(start = 4)


PCTDG.describe()
PCTDG['CANCER_CrudePrev'].corr(PCTDG['TEETHLOST_CrudePrev'])
ax1 = PCTDG.plot.scatter(x = 'CANCER_CrudePrev', y = 'TEETHLOST_CrudePrev')
PCTDG.loc[:, 'CANCER_CrudePrev'].mean()

ax2 = PCTDG.plot.scatter(x = 'TotalPopulation', y = 'CANCER_CrudePrev')
PCTDG['CANCER_CrudePrev'].corr(PCTDG['TotalPopulation'])

PCTDG = PCTDG.rename(columns = {'TRACT': 'CensusTract'})

Merged =  pd.merge(AZ_FARA, PCTDG, on='CensusTract', how = 'left')
Merged_Without_Strings = Merged.drop(columns = ['TEETHLOST_Crude95CI','Geolocation','State','County','StateAbbr','StateDesc','CountyName'])
cols_to_drop = Merged_Without_Strings.columns[Merged_Without_Strings.columns.str.contains('95CI')]
Merged_Without_Strings.drop(cols_to_drop, axis = 1, inplace = True)
Merged_Without_Strings

correlation_matrix = Merged_Without_Strings.corr()
Cancer_Correlations = correlation_matrix['CANCER_CrudePrev']
sorted_correlations = Cancer_Correlations.sort_values(ascending=False)
sorted_correlations = sorted_correlations.to_frame()
sorted_correlations = sorted_correlations.reset_index()
sorted_correlations = sorted_correlations.rename(columns = {'index' : 'Predictor'})
sorted_correlations

ax4 = Merged.plot.scatter(x = 'DENTAL_CrudePrev', y = 'CANCER_CrudePrev')
ax5 = Merged.plot.scatter(x = 'ACCESS2_CrudePrev', y = 'CANCER_CrudePrev')

Merged['Housing by pop'] = Merged['OHU2010']/Merged['TotalPopulation']
ax7 = Merged.plot.scatter(x = 'Housing by pop', y = 'CANCER_CrudePrev')


### New comparisons against obesity/Diabetes

ax8 = Merged.plot.scatter(x = 'TEETHLOST_CrudePrev', y = 'DIABETES_CrudePrev')
ax9 = Merged.plot.scatter(x = 'TEETHLOST_CrudePrev', y = 'OBESITY_CrudePrev')
ax10 = Merged.plot.scatter(x = 'Housing by pop', y = 'DIABETES_CrudePrev')
ax11 = Merged.plot.scatter(x = 'Housing by pop', y = 'OBESITY_CrudePrev')
ax12 = Merged.plot.scatter(x = 'ACCESS2_CrudePrev', y = 'DIABETES_CrudePrev')
ax13 = Merged.plot.scatter(x = 'ACCESS2_CrudePrev', y = 'OBESITY_CrudePrev')
ax14 = Merged.plot.scatter(x = 'DENTAL_CrudePrev', y = 'DIABETES_CrudePrev')
ax15 = Merged.plot.scatter(x = 'DENTAL_CrudePrev', y = 'OBESITY_CrudePrev')
ax16 = Merged.plot.scatter(x = 'PovertyRate', y = 'DIABETES_CrudePrev')
ax17 = Merged.plot.scatter(x = 'PovertyRate', y = 'OBESITY_CrudePrev')
ax18 = Merged.plot.scatter(x = 'MedianFamilyIncome', y = 'DIABETES_CrudePrev')
ax19 = Merged.plot.scatter(x = 'MedianFamilyIncome', y = 'OBESITY_CrudePrev')
### New Time Based Analysis

PLACES2020 = pd.read_csv('../data/PLACES.csv')
PLACES2020 = PLACES2020[PLACES2020['StateAbbr'] == 'AZ']
PLACES2020
PLACES2023 = pd.read_csv('../data/PLACES_2023.csv')
PLACES2023 = PLACES2023[PLACES2023['StateAbbr'] == 'AZ']
PLACES2023
PLACES2024 = pd.read_csv('../data/PLACES_2024.csv')
PLACES2024 = PLACES2024[PLACES2024['StateAbbr'] == 'AZ']
PLACES2024
PLACES2021 = pd.read_csv('../data/PLACES2021.csv')
PLACES2021 = PLACES2021[PLACES2021['StateAbbr'] == 'AZ']
PLACES2021
PLACES2022 = pd.read_csv('../data/PLACES2022.csv')
PLACES2022 = PLACES2022[PLACES2022['StateAbbr'] == 'AZ']
PLACES2022
CountyPop = PLACES2020.groupby('CountyName')['TotalPopulation'].sum().reset_index()
CountyPop = CountyPop.rename(columns = {'TotalPopulation' : 'CountyPop'})
CountyPop

SelectedColumns = ['CountyName','TractFIPS','TotalPopulation','ACCESS2_CrudePrev','CHECKUP_CrudePrev','DENTAL_CrudePrev','DIABETES_CrudePrev','OBESITY_CrudePrev']
PLACES2020_IMP = PLACES2020[SelectedColumns]

PLACES2020_IMP_Renamed = PLACES2020_IMP.add_prefix('2020')
PLACES2020_IMP_Renamed = PLACES2020_IMP_Renamed.rename(columns = {'2020TractFIPS' : 'TractFIPS'})
PLACES2020_IMP_Renamed
PLACES2021_IMP = PLACES2021[SelectedColumns]

PLACES2021_IMP_Renamed = PLACES2021_IMP.add_prefix('2021')
PLACES2021_IMP_Renamed = PLACES2021_IMP_Renamed.rename(columns = {'2021TractFIPS' : 'TractFIPS'})
PLACES2021_IMP_Renamed
PLACES2022_IMP = PLACES2022[SelectedColumns]

PLACES2022_IMP_Renamed = PLACES2022_IMP.add_prefix('2022')
PLACES2022_IMP_Renamed = PLACES2022_IMP_Renamed.rename(columns = {'2022TractFIPS' : 'TractFIPS'})
PLACES2022_IMP_Renamed
PLACES2023_IMP = PLACES2023[SelectedColumns]

PLACES2023_IMP_Renamed = PLACES2023_IMP.add_prefix('2023')
PLACES2023_IMP_Renamed = PLACES2023_IMP_Renamed.rename(columns = {'2023TractFIPS' : 'TractFIPS'})
PLACES2023_IMP_Renamed
PLACES2024_IMP = PLACES2024[SelectedColumns]

PLACES2024_IMP_Renamed = PLACES2024_IMP.add_prefix('2024')
PLACES2024_IMP_Renamed = PLACES2024_IMP_Renamed.rename(columns = {'2024TractFIPS' : 'TractFIPS'})
PLACES2024_IMP_Renamed

Temporal_Merge = pd.merge(PLACES2020_IMP_Renamed, PLACES2021_IMP_Renamed, on='TractFIPS', how = 'left')
Temporal_Merge1 = pd.merge(Temporal_Merge, PLACES2022_IMP_Renamed, on='TractFIPS', how = 'left')
Temporal_Merge12 = pd.merge(Temporal_Merge1, PLACES2023_IMP_Renamed, on='TractFIPS', how = 'left')
Temporal_Merge2 = pd.merge(Temporal_Merge12, PLACES2024_IMP_Renamed, on='TractFIPS', how = 'left')
Temporal_Merge2
Temporal_Merge2['Obesity 2024-2023'] = Temporal_Merge2['2024OBESITY_CrudePrev'] - Temporal_Merge2['2023OBESITY_CrudePrev']
Temporal_Merge2['Obesity 2024-2020'] = Temporal_Merge2['2024OBESITY_CrudePrev'] - Temporal_Merge2['2020OBESITY_CrudePrev']
Temporal_Merge2['Obesity 2023-2020'] = Temporal_Merge2['2023OBESITY_CrudePrev'] - Temporal_Merge2['2020OBESITY_CrudePrev']
Temporal_Merge2['Diabetes 2024-2023'] = Temporal_Merge2['2024DIABETES_CrudePrev'] - Temporal_Merge2['2023DIABETES_CrudePrev']
Temporal_Merge2['Diabetes 2024-2020'] = Temporal_Merge2['2024DIABETES_CrudePrev'] - Temporal_Merge2['2020DIABETES_CrudePrev']
Temporal_Merge2['Diabetes 2023-2020'] = Temporal_Merge2['2023DIABETES_CrudePrev'] - Temporal_Merge2['2020DIABETES_CrudePrev']
ax19 = Temporal_Merge2.plot.scatter(x = 'Obesity 2024-2023', y = 'Obesity 2023-2020')

Obesity2024_2023 = Temporal_Merge2['Obesity 2024-2023'].mean()
Obesity2024_2023
Obesity2024_2020 = Temporal_Merge2['Obesity 2024-2020'].mean()
Obesity2024_2020
Obesity2023_2020 = Temporal_Merge2['Obesity 2023-2020'].mean()
Obesity2023_2020

Diabetes2024_2023 = Temporal_Merge2['Diabetes 2024-2023'].mean()
Diabetes2024_2023
Diabetes2024_2020 = Temporal_Merge2['Diabetes 2024-2020'].mean()
Diabetes2024_2020
Diabetes2023_2020 = Temporal_Merge2['Diabetes 2023-2020'].mean()
Diabetes2023_2020

Temporal_Merge2['ACCESS2_CrudePrev 2024-2023'] = Temporal_Merge2['2024ACCESS2_CrudePrev'] - Temporal_Merge2['2023ACCESS2_CrudePrev']
Temporal_Merge2['ACCESS2_CrudePrev 2024-2020'] = Temporal_Merge2['2024ACCESS2_CrudePrev'] - Temporal_Merge2['2020ACCESS2_CrudePrev']
Temporal_Merge2['ACCESS2_CrudePrev 2023-2020'] = Temporal_Merge2['2023ACCESS2_CrudePrev'] - Temporal_Merge2['2020ACCESS2_CrudePrev']

ACCESS2_CrudePrev2024_2023 = Temporal_Merge2['ACCESS2_CrudePrev 2024-2023'].mean()
ACCESS2_CrudePrev2024_2023
ACCESS2_CrudePrev2024_2020 = Temporal_Merge2['ACCESS2_CrudePrev 2024-2020'].mean()
ACCESS2_CrudePrev2024_2020
ACCESS2_CrudePrev2023_2020 = Temporal_Merge2['ACCESS2_CrudePrev 2023-2020'].mean()
ACCESS2_CrudePrev2023_2020

Temporal_Merge2['DENTAL_CrudePrev 2024-2023'] = Temporal_Merge2['2024DENTAL_CrudePrev'] - Temporal_Merge2['2023DENTAL_CrudePrev']
Temporal_Merge2['DENTAL_CrudePrev 2024-2020'] = Temporal_Merge2['2024DENTAL_CrudePrev'] - Temporal_Merge2['2020DENTAL_CrudePrev']
Temporal_Merge2['DENTAL_CrudePrev 2023-2020'] = Temporal_Merge2['2023DENTAL_CrudePrev'] - Temporal_Merge2['2020DENTAL_CrudePrev']

DENTAL_CrudePrev2024_2023 = Temporal_Merge2['DENTAL_CrudePrev 2024-2023'].mean()
DENTAL_CrudePrev2024_2023
DENTAL_CrudePrev2024_2020 = Temporal_Merge2['DENTAL_CrudePrev 2024-2020'].mean()
DENTAL_CrudePrev2024_2020
DENTAL_CrudePrev2023_2020 = Temporal_Merge2['DENTAL_CrudePrev 2023-2020'].mean()
DENTAL_CrudePrev2023_2020

#weighted by county information

PLACES2020_IMP1 = pd.merge(PLACES2020_IMP, CountyPop, on = 'CountyName', how = 'left')
PLACES2020_IMP1['WeightedDiabetes'] = PLACES2020_IMP1['DIABETES_CrudePrev'] * PLACES2020_IMP1['TotalPopulation']
PLACES2020_IMP1['WeightedObesity'] = PLACES2020_IMP1['OBESITY_CrudePrev'] * PLACES2020_IMP1['TotalPopulation']
PLACES2020_IMP1
PLACES2020_IMP2 = PLACES2020_IMP1.groupby('CountyName')['WeightedDiabetes'].sum().reset_index()
PLACES2020_IMP2
PLACES2020_IMP3 = PLACES2020_IMP1.groupby('CountyName')['WeightedObesity'].sum().reset_index()
PLACES2020_IMP3
PLACES2020_IMP4 = pd.merge(PLACES2020_IMP2, PLACES2020_IMP3, on = 'CountyName', how = 'left')
PLACES2020_IMP4
PLACES2020_IMP5 = pd.merge(PLACES2020_IMP4, CountyPop, on = 'CountyName', how = 'left')
PLACES2020_IMP5['WeightedDiabetes/CountyPop'] = PLACES2020_IMP5['WeightedDiabetes']/PLACES2020_IMP5['CountyPop'].round(4)
PLACES2020_IMP5['WeightedObesity/CountyPop'] = PLACES2020_IMP5['WeightedObesity']/PLACES2020_IMP5['CountyPop'].round(4)
PLACES2020_IMP5['WeightedDiabetes/CountyPop'] = PLACES2020_IMP5['WeightedDiabetes/CountyPop'].round(4)
PLACES2020_IMP5['WeightedObesity/CountyPop'] = PLACES2020_IMP5['WeightedObesity/CountyPop'].round(4)
PLACES2020_IMP5_Renamed = PLACES2020_IMP5.add_prefix('2020')
PLACES2020_IMP5_Renamed = PLACES2020_IMP5_Renamed.rename(columns = {'2020CountyName' : 'CountyName'})
PLACES2020_Weighted = PLACES2020_IMP5_Renamed.drop(['2020WeightedDiabetes','2020WeightedObesity','2020CountyPop'], axis = 1)
PLACES2020_Weighted

PLACES2021_IMP1 = pd.merge(PLACES2021_IMP, CountyPop, on = 'CountyName', how = 'left')
PLACES2021_IMP1['WeightedDiabetes'] = PLACES2021_IMP1['DIABETES_CrudePrev'] * PLACES2021_IMP1['TotalPopulation']
PLACES2021_IMP1['WeightedObesity'] = PLACES2021_IMP1['OBESITY_CrudePrev'] * PLACES2021_IMP1['TotalPopulation']
PLACES2021_IMP1
PLACES2021_IMP2 = PLACES2021_IMP1.groupby('CountyName')['WeightedDiabetes'].sum().reset_index()
PLACES2021_IMP2
PLACES2021_IMP3 = PLACES2021_IMP1.groupby('CountyName')['WeightedObesity'].sum().reset_index()
PLACES2021_IMP3
PLACES2021_IMP4 = pd.merge(PLACES2021_IMP2, PLACES2021_IMP3, on = 'CountyName', how = 'left')
PLACES2021_IMP4
PLACES2021_IMP5 = pd.merge(PLACES2021_IMP4, CountyPop, on = 'CountyName', how = 'left')
PLACES2021_IMP5['WeightedDiabetes/CountyPop'] = PLACES2021_IMP5['WeightedDiabetes']/PLACES2021_IMP5['CountyPop'].round(4)
PLACES2021_IMP5['WeightedObesity/CountyPop'] = PLACES2021_IMP5['WeightedObesity']/PLACES2021_IMP5['CountyPop'].round(4)
PLACES2021_IMP5['WeightedDiabetes/CountyPop'] = PLACES2021_IMP5['WeightedDiabetes/CountyPop'].round(4)
PLACES2021_IMP5['WeightedObesity/CountyPop'] = PLACES2021_IMP5['WeightedObesity/CountyPop'].round(4)
PLACES2021_IMP5_Renamed = PLACES2021_IMP5.add_prefix('2021')
PLACES2021_IMP5_Renamed = PLACES2021_IMP5_Renamed.rename(columns = {'2021CountyName' : 'CountyName'})
PLACES2021_Weighted = PLACES2021_IMP5_Renamed.drop(['2021WeightedDiabetes','2021WeightedObesity','2021CountyPop'], axis = 1)
PLACES2021_Weighted

PLACES2022_IMP1 = pd.merge(PLACES2022_IMP, CountyPop, on = 'CountyName', how = 'left')
PLACES2022_IMP1['WeightedDiabetes'] = PLACES2022_IMP1['DIABETES_CrudePrev'] * PLACES2022_IMP1['TotalPopulation']
PLACES2022_IMP1['WeightedObesity'] = PLACES2022_IMP1['OBESITY_CrudePrev'] * PLACES2022_IMP1['TotalPopulation']
PLACES2022_IMP1
PLACES2022_IMP2 = PLACES2022_IMP1.groupby('CountyName')['WeightedDiabetes'].sum().reset_index()
PLACES2022_IMP2
PLACES2022_IMP3 = PLACES2022_IMP1.groupby('CountyName')['WeightedObesity'].sum().reset_index()
PLACES2022_IMP3
PLACES2022_IMP4 = pd.merge(PLACES2022_IMP2, PLACES2022_IMP3, on = 'CountyName', how = 'left')
PLACES2022_IMP4
PLACES2022_IMP5 = pd.merge(PLACES2022_IMP4, CountyPop, on = 'CountyName', how = 'left')
PLACES2022_IMP5['WeightedDiabetes/CountyPop'] = PLACES2022_IMP5['WeightedDiabetes']/PLACES2022_IMP5['CountyPop'].round(4)
PLACES2022_IMP5['WeightedObesity/CountyPop'] = PLACES2022_IMP5['WeightedObesity']/PLACES2022_IMP5['CountyPop'].round(4)
PLACES2022_IMP5['WeightedDiabetes/CountyPop'] = PLACES2022_IMP5['WeightedDiabetes/CountyPop'].round(4)
PLACES2022_IMP5['WeightedObesity/CountyPop'] = PLACES2022_IMP5['WeightedObesity/CountyPop'].round(4)
PLACES2022_IMP5_Renamed = PLACES2022_IMP5.add_prefix('2022')
PLACES2022_IMP5_Renamed = PLACES2022_IMP5_Renamed.rename(columns = {'2022CountyName' : 'CountyName'})
PLACES2022_Weighted = PLACES2022_IMP5_Renamed.drop(['2022WeightedDiabetes','2022WeightedObesity','2022CountyPop'], axis = 1)
PLACES2022_Weighted

PLACES2023_IMP1 = pd.merge(PLACES2023_IMP, CountyPop, on = 'CountyName', how = 'left')
PLACES2023_IMP1['WeightedDiabetes'] = PLACES2023_IMP1['DIABETES_CrudePrev'] * PLACES2023_IMP1['TotalPopulation']
PLACES2023_IMP1['WeightedObesity'] = PLACES2023_IMP1['OBESITY_CrudePrev'] * PLACES2023_IMP1['TotalPopulation']
PLACES2023_IMP1
PLACES2023_IMP2 = PLACES2023_IMP1.groupby('CountyName')['WeightedDiabetes'].sum().reset_index()
PLACES2023_IMP2
PLACES2023_IMP3 = PLACES2023_IMP1.groupby('CountyName')['WeightedObesity'].sum().reset_index()
PLACES2023_IMP3
PLACES2023_IMP4 = pd.merge(PLACES2023_IMP2, PLACES2023_IMP3, on = 'CountyName', how = 'left')
PLACES2023_IMP4
PLACES2023_IMP5 = pd.merge(PLACES2023_IMP4, CountyPop, on = 'CountyName', how = 'left')
PLACES2023_IMP5['WeightedDiabetes/CountyPop'] = PLACES2023_IMP5['WeightedDiabetes']/PLACES2023_IMP5['CountyPop'].round(4)
PLACES2023_IMP5['WeightedObesity/CountyPop'] = PLACES2023_IMP5['WeightedObesity']/PLACES2023_IMP5['CountyPop'].round(4)
PLACES2023_IMP5['WeightedDiabetes/CountyPop'] = PLACES2023_IMP5['WeightedDiabetes/CountyPop'].round(4)
PLACES2023_IMP5['WeightedObesity/CountyPop'] = PLACES2023_IMP5['WeightedObesity/CountyPop'].round(4)
PLACES2023_IMP5_Renamed = PLACES2023_IMP5.add_prefix('2023')
PLACES2023_IMP5_Renamed = PLACES2023_IMP5_Renamed.rename(columns = {'2023CountyName' : 'CountyName'})
PLACES2023_Weighted = PLACES2023_IMP5_Renamed.drop(['2023WeightedDiabetes','2023WeightedObesity','2023CountyPop'], axis = 1)
PLACES2023_Weighted


PLACES2024_IMP1 = pd.merge(PLACES2024_IMP, CountyPop, on = 'CountyName', how = 'left')
PLACES2024_IMP1['WeightedDiabetes'] = PLACES2024_IMP1['DIABETES_CrudePrev'] * PLACES2024_IMP1['TotalPopulation']
PLACES2024_IMP1['WeightedObesity'] = PLACES2024_IMP1['OBESITY_CrudePrev'] * PLACES2024_IMP1['TotalPopulation']
PLACES2024_IMP1
PLACES2024_IMP2 = PLACES2024_IMP1.groupby('CountyName')['WeightedDiabetes'].sum().reset_index()
PLACES2024_IMP2
PLACES2024_IMP3 = PLACES2024_IMP1.groupby('CountyName')['WeightedObesity'].sum().reset_index()
PLACES2024_IMP3
PLACES2024_IMP4 = pd.merge(PLACES2024_IMP2, PLACES2024_IMP3, on = 'CountyName', how = 'left')
PLACES2024_IMP4
PLACES2024_IMP5 = pd.merge(PLACES2024_IMP4, CountyPop, on = 'CountyName', how = 'left')
PLACES2024_IMP5['WeightedDiabetes/CountyPop'] = PLACES2024_IMP5['WeightedDiabetes']/PLACES2024_IMP5['CountyPop'].round(4)
PLACES2024_IMP5['WeightedObesity/CountyPop'] = PLACES2024_IMP5['WeightedObesity']/PLACES2024_IMP5['CountyPop'].round(4)
PLACES2024_IMP5['WeightedDiabetes/CountyPop'] = PLACES2024_IMP5['WeightedDiabetes/CountyPop'].round(4)
PLACES2024_IMP5['WeightedObesity/CountyPop'] = PLACES2024_IMP5['WeightedObesity/CountyPop'].round(4)
PLACES2024_IMP5_Renamed = PLACES2024_IMP5.add_prefix('2024')
PLACES2024_IMP5_Renamed = PLACES2024_IMP5_Renamed.rename(columns = {'2024CountyName' : 'CountyName'})
PLACES2024_Weighted = PLACES2024_IMP5_Renamed.drop(['2024WeightedDiabetes','2024WeightedObesity','2024CountyPop'], axis = 1)
PLACES2024_Weighted

WeightedMerged = pd.merge(PLACES2020_Weighted,PLACES2021_Weighted, on = 'CountyName', how = 'left')
WeightedMerged1 = pd.merge(WeightedMerged,PLACES2022_Weighted, on = 'CountyName', how = 'left')
WeightedMerged12 = pd.merge(WeightedMerged1,PLACES2023_Weighted, on = 'CountyName', how = 'left')
WeightedMerged2 = pd.merge(WeightedMerged12, PLACES2024_Weighted, on = 'CountyName', how = 'left')
WeightedMerged2

WeightedMerged2['Obesity 2024-2023'] = WeightedMerged2['2024WeightedObesity/CountyPop'] - WeightedMerged2['2023WeightedObesity/CountyPop']
WeightedMerged2['Obesity 2023-2022'] = WeightedMerged2['2023WeightedObesity/CountyPop'] - WeightedMerged2['2022WeightedObesity/CountyPop']
WeightedMerged2['Obesity 2022-2021'] = WeightedMerged2['2022WeightedObesity/CountyPop'] - WeightedMerged2['2021WeightedObesity/CountyPop']
WeightedMerged2['Obesity 2021-2020'] = WeightedMerged2['2021WeightedObesity/CountyPop'] - WeightedMerged2['2020WeightedObesity/CountyPop']
WeightedMerged2['Diabetes 2024-2023'] = WeightedMerged2['2024WeightedDiabetes/CountyPop'] - WeightedMerged2['2023WeightedDiabetes/CountyPop']
WeightedMerged2['Diabetes 2023-2022'] = WeightedMerged2['2023WeightedDiabetes/CountyPop'] - WeightedMerged2['2022WeightedDiabetes/CountyPop']
WeightedMerged2['Diabetes 2022-2021'] = WeightedMerged2['2022WeightedDiabetes/CountyPop'] - WeightedMerged2['2021WeightedDiabetes/CountyPop']
WeightedMerged2['Diabetes 2021-2020'] = WeightedMerged2['2021WeightedDiabetes/CountyPop'] - WeightedMerged2['2020WeightedDiabetes/CountyPop']
WeightedMerged2