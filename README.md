[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# ![](images/uofa.png) INFO 698 : Summer 2025

# GeoHealthAI

### Overview

GeoHealthAI quantifies and traces the overlap of food access, poverty, and chronic disease in Arizona—with particular attention to Native Nations—using tract-level data from CDC PLACES, the USDA Food Access Research Atlas, and socioeconomic indicators. Leveraging PySpark and Pandas, we merged our sources by tract FIPS and conducted descriptive analyses, correlation matrices, linear regressions, and z-score flagging to identify high-burden tracts. We created an interactive heatmap dashboard to highlight priority areas experiencing higher rates of chronic disease such as obesity and diabetes. Beyond data analysis, we will pair the analytics with interviews that center Native perspectives, providing culturally grounded context for community-informed public health action.

### Motivation

We started this because it’s hard to fix what you can’t see. In many Arizona communities—especially rural and tribal areas—healthy food access and healthcare can be far away, and the data is scattered. By putting it all on one clear map and listening to local voices, we want to help communities spot gaps and act faster.

### What We’re Trying to Do

- Quantify and map how food access and socioeconomic disadvantage relate to obesity/diabetes across Arizona census tracts, with special focus on Native Nations and rural–urban differences.
- Identify high-burden hotspots using a composite Food Desert Score and multi-year trends to guide public health initiatives. 
- Deliver an interactive dashboard with a heat map to display our results, giving actionable insights to policymakers and concerned parties. 

### Our Data Sources

We worked with two main datasets:
- CDC PLACES Census Tract Data (2020–2024 releases): Provides modeled estimates of chronic disease prevalence at the census tract level. Datasets reflect Behavioral Risk Factor Surveillance System (BRFSS) data from two years prior. The 2020-2024 released datasets cover the years 2018-2020, respectively.
- USDA Food Access Research Atlas (FARA): Identifies tracts with low access to grocery stores, often used to define food deserts. Includes tract population counts and demographic data. Data reflects 2010 census tract information.

These publicly available datasets collectively cover 1,516–1,520 census tracts across Arizona, including rural, metro, and tribal lands.These datasets reflect data from 2018-2022, effectively capturing pre-pandemic, pandemic, and post-pandemic health and disease prevalence within Arizona communities. 


### Team Members

| **Name**                  | **Email**                     |
|---------------------------|-------------------------------|
| Remi Hendershott          | [emoryh@arizona.edu](mailto:emoryh@arizona.edu) |
| Sarah Gilbride            | [sarahgilbride@arizona.edu](mailto:sarahgilbride@arizona.edu) |
| Cole Johnson              | [cwjohn13@arizona.edu](mailto:cwjohn13@arizona.edu) |

## Repository Organization

Folders & Files 

- `Working_Files`: Contains individual working files for each team mate; used for cleaning data & making visuals.
- `data`: Includes all datasets used for analysis.
- `index.qmd`: Holds the final project report with infographics included. 
- `dashboard.qmd`: Visualizations like our interactive heatmap are displayed here and sorted by tabs. 
- `code.qmd`: Finalized script for cleaning, analyzing, and visualizing data.
- `proposal.qmd`: Contains the initial project proposal document.
- `about.qmd`: Team members information for this project. 
- `images`: Visualizations we created and used.
- `_quarto.yml`: File to set up Quarto wesbite & dashboard.

        

