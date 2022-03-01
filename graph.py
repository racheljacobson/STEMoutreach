#pip install
# #import nba rookie data from excel
import pandas as pd 

#this is configuration for reading the data but we have not implemented this yet
data= pd.read_excel (r'C:\Users\Rachel\Documents\nba rookie data.xlsx', sheet_name='nba rookie data')
dfStrength = pd.DataFrame(data, columns= ['Strength'])
dfVertical = pd.DataFrame(data, columns= ['Vertical'])    
dfQuickness = pd.DataFrame(data, columns= ['Quickness'])
dfAgility = pd.DataFrame(data, columns= ['Agility'])  
dfSpeed = pd.DataFrame(data, columns= ['Speed'])                         
#print (df)

#for radar chart configuration 
import plotly.graph_objects as go
categories = ['stength', 'vertical', 'quickness', 
              'agility', 'speed'] #these categories are from nba rookie data 
Fig = go.Figure()

#columns G-L

                       #this is an example graph with sample data. Will need to use imported excel data 
Fig.add_trace(go.Scatterpolar( #with data from participant 
  r=[8, 27.5, 2.75, 10.27, 3.28],
  theta=categories,
      fill='toself',
      name='Combine 1'
))
                       
Fig.add_trace(go.Scatterpolar( #comparison data from our saved files determined based on sex and sport
  r=[17, 35.5, 2.69, 10.82, 3.15],
  theta=categories,
      fill='toself',
      name='Combine 2'
))
                       
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 40]
    )),
  showlegend=False
)

fig.show()
 
                       
#code generated with example from https://plotly.com/python/radar-chart/