
## KENYA FOOD PRICE EARLY WARNING SYSTEM.

## OVERVIEW

The project entails developing a predictive model to assist in determining food prices with an aim of minimizing effects of price spikes such as food insecurity in Kenya.

Applications include provision of:

- Advance warning for optimal procurement timing for Food Aid Organizations such as WFP,Red Cross etc.
- Market intelligence that assist farmers and other stakeholders make optimal selling decisions.
- Advice to farmers and relevant stakeholders on crops choices based on weather,soil and market demand. 
- Guidance in budgeting/ financial spending especially for vulnerable households.


### OBJECTIVES

1)To Identify factors that have impact on food prices. 

2)To develop a predictive model that uses above identified factors to predict food prices 2-3 months in advance.

3)To create a deployment model that enables target audiences such as farmers effectively and efficiently practise their trade.

## DATA UNDERSTANDING AND ANALYSIS
### Source of Data

The primary dataset for this project is the WFP Kenya Food Prices Database, obtained from the Humanitarian Data Exchange (HDX). This dataset contains over 50,000 monthly food price records collected between 2006 and 2024, covering more than 200 local markets across all 47 counties in Kenya. It includes prices for 15+ key food commodities, such as maize, beans, rice, wheat, and sorghum. To enhance predictive capability, the project integrates a range of supplementary datasets: Rainfall and weather data are sourced from the CHIRPS (Climate Hazards Group InfraRed Precipitation) dataset and the Kenya Meteorological Department (KMD), Economic indicators collected from the Kenya National Bureau of Statistics (KNBS) and the Central Bank of Kenya (CBK) and Geospatial data from OpenStreetMap (OSM) and the Kenya Revenue Authority (KRA).  

### Description of Data

The main features analyzed after merging the above data sets are;

- rainfall_mm
- month
- year
- commodity_code
- market_code
- admin1_code
- admin2_code

Visualization of Average Commodity Prices Over Time

![alt text](image-1.png)


Visualization of Price Distribution Per Commodity

![alt text](image-2.png)

Data cleaning entailed dropping duplicates as well as the null values of the main columns,i.e price, rainfall_mm, commodity_id.

## MODELING
The models used: NeuralNet, Ridge, Random Forest, and Gradient Boosting are trained and evaluated on the same dataset.
The best model is selected based on R2 score and saved for deployment.

## EVALUATION
The results based on regression metrics analysis are as follows:

Model Comparison:

                Model               MAE        RMSE       R2

                RandomForest       385.97     801.86     0.921

                GradientBoosting   957.77    1412.12     0.754

                NeuralNet          1561.81   2232.69     0.384

                Ridge              2048.13   2720.92     0.086

Visualization of Model R2 Scores

![alt text](image.png)


## RECOMMENDATIONS
- Random Forest model had the highest R2 score therefore the best for deployment.
- Further fine tuning can be done to improve model perfomance.




