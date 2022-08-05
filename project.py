import plotly.figure_factory as ff 
import pandas as pd 
import csv 

csv=pd.read_csv('P108.csv')

Avgrating=csv['Avg Rating'],tolist()
graph=ff.create_distplot([Avgrating],['Ratings'])

graph.show()