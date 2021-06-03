# Importing all the necessary Python Libraries 
import pycountry
import plotly.express as px
import pandas as pd

#Exrtracting the data from the GitHub COVID-19 Data
database = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
data_1 = pd.read_csv(database)
print(data_1)
