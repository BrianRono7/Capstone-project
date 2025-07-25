# Kenya Food Price Early Warning System  
### Capstone Project – *Synergy Creators*

---

## Executive Summary

The **Kenya Food Price Early Warning System** is an integrated, data-driven platform developed to predict food price surges and guide climate-resilient agricultural decisions across Kenya. In light of increasing climate variability, market disruptions, and economic shocks, this system seeks to empower farmers, support policymakers, and strengthen national food security frameworks by providing timely, predictive insights grounded in real-world data.

Through the application of machine learning, climatological analysis, and economic modeling, the platform anticipates price spikes up to three months in advance and recommends optimal crops based on environmental and market conditions. It aligns with national strategies such as Kenya Vision 2030 and the Agricultural Sector Transformation and Growth Strategy (ASTGS).

---

## 1. Background

Kenya's agri-food system is under significant stress due to unpredictable climatic events, volatile commodity markets, and economic instability. Over 3.5 million citizens are currently facing acute food insecurity, a figure projected to rise without timely, evidence-based interventions. Agriculture, which employs over 70% of the rural workforce and contributes approximately one-third of the country’s GDP, remains largely subsistence-based and poorly informed by real-time data.

Currently, institutional responses to food insecurity are predominantly reactive—implemented after crop failures or price spikes have already occurred—resulting in diminished impact, increased humanitarian costs, and missed intervention opportunities. There exists a critical need for an anticipatory, predictive solution capable of informing proactive decision-making.

---

## 2. Problem Statement

The absence of predictive infrastructure in Kenya’s food security ecosystem has resulted in:

- Unstable incomes for smallholder farmers
- Increased vulnerability of low-income households to hunger
- Delayed public procurement and late subsidy implementation
- Suboptimal resource allocation by humanitarian agencies

For instance, a 30% increase in the price of maize may plunge over half a million individuals into acute hunger in under a month. Without early warning systems, stakeholders lack the foresight required to mitigate such impacts.

---

## 3. Project Objectives

### i. Food Price Forecasting  
Develop robust machine learning models to predict food price spikes (>20%) two to three months in advance, leveraging climatic, market, and economic datasets.

### ii. Crop Recommendation Engine  
Build a recommendation system that advises farmers on optimal crop choices based on soil suitability, historical rainfall patterns, and current market dynamics.

### iii. Farmer Empowerment  
Deliver location-specific, predictive insights to smallholder farmers, enabling more informed decision-making, reduced risk, and improved income stability.

### iv. Policy and Institutional Support  
Enable timely governmental responses via early warning triggers, informing the deployment of strategic grain reserves, subsidies, and emergency declarations.

### v. Climate-Smart Agriculture Promotion  
Align agricultural recommendations with seasonal forecasts and ecological realities to encourage resilient farming practices.

### vi. National Development Alignment  
Support long-term national development strategies including **Kenya Vision 2030** and **ASTGS** through the deployment of digital agricultural solutions.

---

## 4. Stakeholder Mapping

This system has been designed to serve a broad and diverse network of stakeholders, each with unique decision-making needs and responsibilities:

| Stakeholder Group               | Application of the System                                                  |
|----------------------------------|-----------------------------------------------------------------------------|
| **Smallholder Farmers**         | Real-time insights on crop selection, planting windows, and price outlooks |
| **Vulnerable Households**       | Early warnings for food budgeting and household-level resilience planning  |
| **Government & Policymakers**   | Data-informed activation of food subsidies and reserves                    |
| **Humanitarian Organizations**  | Advance planning for aid procurement and distribution                      |
| **Development Partners & Donors**| Evidence-based resource targeting and food security trend monitoring        |
| **Agribusinesses & Traders**    | Market intelligence and volatility analysis for logistics and pricing      |

---

## 5. Methodological Approach

### 5.1 Data Sources
- **Market Price Data**: National food price datasets across counties and commodities  
- **Climatic Data**: CHIRPS v3 rainfall estimates (1981–present), covering daily and monthly precipitation  
- **Economic Indicators**: Inflation rates, input costs, and trade patterns  
- **Geospatial Data**: Administrative boundaries, ecological zones, and market access routes

### 5.2 Tools & Technologies
- **Programming**: Python (Pandas, NumPy, Scikit-learn, XGBoost)
- **Visualization**: Matplotlib, Seaborn, GeoPandas, Folium
- **Model Management**: MLflow for experiment tracking
- **Deployment**: Streamlit for interactive dashboards
- **Version Control**: Git/GitHub

---

## 6. CHIRPS v3 Rainfall Dataset

The **Climate Hazards Group InfraRed Precipitation with Station Data (CHIRPS)** is utilized to model precipitation anomalies and their effects on agricultural yield and price volatility. CHIRPS v3 offers:

- Spatial resolution of ~5 km  
- Daily and monthly temporal granularity  
- Integration of infrared satellite imagery with ground-based rainfall data  

Its inclusion is critical for modeling climate variability and forecasting agricultural conditions in a localized context.

---
