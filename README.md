[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# ![](images/uofa.png)INFO 698 : Summer 2025

# GeoHealthAI

### Overview

GeoHealthAI quantifies and maps the overlap of food access, poverty, and chronic disease in Arizona—with particular attention to Native Nations—using tract-level data from CDC PLACES, the USDA Food Access Research Atlas, and socioeconomic indicators. Using PySpark and Pandas, we integrate sources by tract FIPS and conduct descriptive analyses, correlation matrices, linear regressions, and z-score flagging to identify high-burden tracts. We deploy an interactive heatmap dashboard to surface priority areas and pair the analytics with interviews that center Native perspectives, providing culturally grounded context for community-informed public health action.

### Motivation

We started this because it’s hard to fix what you can’t see. In many Arizona communities—especially rural and tribal areas—healthy food and care can be far away, and the data is scattered. By putting it all on one clear map and listening to local voices, we want to help communities spot gaps and act faster.

### What We’re Trying to Do

- Quantify and map how food access and socioeconomic disadvantage relate to obesity/diabetes across Arizona census tracts, with special focus on Native Nations and rural–urban differences.
- Identify high-burden hotspots using a composite Food Desert Score and multi-year trends to guide public health initiatives. 
- Deliver an interactive dashboard with a heat map, to display our results, giving actionable insights to policymakers and concerned parties. 

### Our Data Sources

We worked with two main datasets:
- CDC PLACES Census Tract Data (2020–2024 releases): Provides modeled estimates of chronic disease prevalence at the census tract level. Datasets reflect Behavioral Risk Factor Surveillance System (BRFSS) data from two years prior. The 2020-2024 released datasets cover the years 2018-2020, respectively.
- USDA Food Access Research Atlas (FARA): Identifies tracts with low access to grocery stores, often used to define food deserts. Includes tract population counts and demographic data. Data reflects 2010 census tract information.

These publicly available datasets collectively cover 1,516–1,520 census tracts across Arizona, including rural, metro, and tribal lands.These datasets reflect data from 2018-2022, effectively capturing pre-pandemic, pandemic, and post-pandemic health and disease prevalence within Arizona communities. Utilizing multiple years of CDC Places series data allows for the added element of time as an analysis option when exploring the relationship between food accessibility and chronic health outcomes within these tracts.


### Team Members

| **Name**                  | **Email**                     |
|---------------------------|-------------------------------|
| Remi Hendershott          | [emoryh@arizona.edu](mailto:emoryh@arizona.edu) |
| Sarah Gilbride            | [sarahgilbride@arizona.edu](mailto:sarahgilbride@arizona.edu) |
| Cole Johnson              | [cwjohn13@arizona.edu](mailto:cwjohn13@arizona.edu) |

## File Organization

    analysis/
    |
    ├── logs/
    │   └── log.md          # log of any progress or relevant information
    |
    ├── figures/            # location of the figures produced for the manuscript
    |
    ├── data/
    |   ├── rawData/        # data obtained from elsewhere
    │   └── derivedData/    # data generated from rawData/ and scripts.*
    |   
    └── supplementaryMaterials/
        ├── supplementaryFigures/     
        |                   # supplementary figures for the main manuscript
        └── supplementaryTables/      
                            # supplementary tables for the main manuscript 
    
    src                     # scripts to run in the following order (also see associated README.md)
    └── script.*            # hypothetical script used to wrangle the raw data, produce figures, analyses, and supplementary materials

        

