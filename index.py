import pycountry
import plotly.express as px
import pandas as pd

database = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
data_1 = pd.read_csv(database)

countries = data_1['Country'].unique().tolist()
country_codes = {}
for country in countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)
        code = country_data[0].alpha_3
        country_codes.update({country: code})
    except:
        country_codes.update({country: ' '})
for key, values in country_codes.items():
    data_1.loc[(data_1.Country == key), 'ISO_Code'] = values

figure = px.choropleth(data_frame=data_1,
                       title = "Hariket Sheth: Plotting COVID-19 Timeline",
                       locations="ISO_Code",
                       color="Confirmed",
                       hover_name="Country",
                       color_continuous_scale="haline",
                       animation_frame="Date")
figure.show()
