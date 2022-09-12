#!/usr/bin/env python
# coding: utf-8

# Import libraries

# In[1]:



import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
from jupyter_dash import JupyterDash
import plotly.graph_objects as go
import plotly.express as px
import json
from urllib.request import urlopen
import numpy as np
from geojson_rewind import rewind


# In[2]:


#Load GeoJson
with urlopen('https://raw.githubusercontent.com/plummy95/1312306/main/Local_Administrative_Units_Level_1_(December_2015)_Boundaries%20(1).json') as response:
    counties = json.load(response)


# Import datasets

# In[3]:


counties_corrected=rewind(counties,rfc7946=False)

import io
quali=pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualificationpercentage.csv')
df=pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/totaldata.csv')
full=pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/totaldata.csv')
eastmidlands = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/East%20Midlands.csv')
eastengland = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/East%20of%20England.csv')
northeast = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/North%20East.csv')
northwest = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/North%20West.csv')
southeast = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/South%20East.csv')
southwest = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/South%20West.csv')
westmidlands = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/West%20midlands.csv')
london = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/london.csv')
yorkshirehumber = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/yorkshire%20and%20the%20humber.csv')
qualbar = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualificationbar2020.csv')
qualbarlondon = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarLondon.csv')
qualbarnortheast = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarNortheast.csv')
qualbarnorthwest = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarNorthwest.csv')
qualbarsoutheast = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarSoutheast.csv')
qualbarsouthwest = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarSouthwest.csv')
qualbarwestmids = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarWestMids.csv')
qualbaryorkshire = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbarYorkshire.csv')
qualbareastengland = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbareastengland.csv')
qualbareastmid = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/qualbareastmid.csv')
meanwage = df['weeklygrosspaymean'].tail(1).iloc[0].astype(float)
meanwageEM = eastmidlands['weeklygrosspaymean']
fullmeanwage = df['weeklygrosspaymean']
bottom20prev =  pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/bottom20prevalence.csv')
bottom20qual = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/bottom20qual.csv')
bottom20wage = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/bottom20wage.csv')
top20prev = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/top20prevalence.csv')
top20qual = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/top20qualifcation.csv')
top20wage = pd.read_csv('https://raw.githubusercontent.com/plummy95/1312306/main/top20wage.csv')


dft = df.rename({"lau115nm" : "Local Authority", "predictedprevalence" : "Predicted Autism Prevalence", "percentageprevalence" : "Predicted Autism Percentage", 
                                    "Noqualifications" : "No Qualifications",
                                    "Percentagenoqualification" : "No Qualification percentage", "Level1qualifications" : "Level 1 Qualifications",  "percentagelevel1" : " Level 1 Qualification Percentage", 
                                    "Level2qualifications" : "Level 2 Qualifications", "percentagelevel2" : "Level 2 Qualification Percentage",
                                    "percentageapprenticeship" : "Apprenticeship Qualification Percentage", "Level3qualifications" : "Level 3 Qualifications",
                                    "percentagelevel3" : "Level 3 Qualification Percentage", "Level4qualificationsandabove" : "Level 4 Qualifications",
                                    "percentagelevel4andabove" : "Level 4 Qualification Percentage", "Otherqualifications" : "Other Qualifications",
                                    "percentageotherqualifications" : "Other Qualification Percentage", "weeklygrosspaymean" : "Mean Weekly Gross Pay"}, axis=1)

qualifications= df[['Noqualifications','Level1qualifications','Level2qualifications','Level3qualifications', 'Level4qualificationsandabove', 'Apprenticeship', 'Otherqualifications']].copy

yearqual = 2020
years = df['lau115nm'].unique()
years2 = df['year'].unique()
yearsplit = df.groupby('year')
[yearsplit.get_group(x) for x in yearsplit.groups]
pie_melt_select = quali
pie_melt_select = pd.melt(pie_melt_select, id_vars=["lau115nm", "region"], value_vars=['" % no qualification"', '"% level 1 qualification"', '" % level 2 qualification"', '" % apprenticeship"', 
                                                                  '" % level 3 qualification"', '" % level 4 and above"', '" % other qualifications"'], var_name="namepie", value_name="valuepie")
print(pie_melt_select)

pie_melt_prevalence = full
pie_melt_prevalence = pd.melt(pie_melt_prevalence, id_vars=["lau115nm", "region", "year"], value_vars=["predictedprevalence", "population"], var_name="namepie2", value_name="valuepie2")
all_options = {
    'area' : df['lau115nm'],
    'yearly' : df['year']
}
    


# In[4]:


print(pie_melt_prevalence)


# In[5]:


mergeregion = df["region"].unique()


# In[6]:


tab_options = []
for location in df['lau115nm'].unique():
    tab_options.append({'label':str(location), 'value':location})









# Create choropleth map for predicted prevalence with animated timescale frame

# In[10]:


fig2020prev = px.choropleth(df, 
                    geojson=counties_corrected,
                    locations='lau115cd',
                    featureidkey="properties.lau115cd",
                    projection='airy',
                    color='percentageprevalence',
                    color_continuous_scale="Turbo",
                    range_color=[0.50, 1.0],
                    labels={'lau115nm':'percentage prevalence'},
                    hover_name="lau115nm",
                    animation_frame='year',
                    title = 'Changes in predicted autism prevalence in England between 2020 to 2040',        
                    scope="europe",
                            )
                

fig2020prev.update_geos(fitbounds="locations", visible=False)
fig2020prev.update_layout(autosize=False,
                  width=1060,
                  height=800,
                  margin={"r":60,"t":100,"l":60,"b":100})



# Creating Dashboard application

# In[11]:


app =dash.Dash(__name__)


# Loading data

# Setup of the application's layout

# In[24]:


app.layout = html.Div([
    html.Div([
        html.H1("Autism Prevalence and Socioeconomic Status"),
        html.H2('The aim of this dashboard is to explore potential links between autism prevalence in the adult population aged 18-64 years and socioeconomic factors such as educational status and income in different parts of England',
                   style={'color' : 'rgb(33 36 35)'}),
        html.H3("Predicted Autism Prevalence has been obtained through the Projecting Adult Needs and Service Information (POPPI v14.2 Jan 2022.)"
               )
        
    ], className='title'),
    
    html.Div([
        dcc.Tabs(id="tabs", value='tab1', children=[
            dcc.Tab(label='Tab One', children=[
                html.Div(children=[
                    dbc.Row(
                        [
                            html.Div(children=[
                                dbc.Row (
                                    [
                                        dbc.Col(html.Div(" This choropleth map explores predicted autism prevalence across England between the years 2020 until 2040. "),
                                                width = 4
                                               )
                                    ]
                                )
                            ], className = 'choropleth_text')
                                        
                        ]
                    ),
                    
                    dbc.Row(
                        [
                            dbc.Col(dcc.Graph(figure=fig2020prev),
                                    width=100, lg={'size' : 10, "offset" : 0, 'order' : 'first'}
                                   ),
                        ]
                    ),
                    dbc.Row(
                        [
                            html.Div(children=[
                                dbc.Row(
                                    [
                                        dbc.Col(html.H3("Wordcloud of Terminology Relating to Socioeconomic Status"),
                                               ),
                                        dbc.Col(html.Img(src=app.get_asset_url('wordcloud.png'), style={'position' : 'relative', 'width' : '100%', 'left' : '0px', 'top' : '0px'}),
                                               ),
                                    
                                    ]
                                )
                            ], className = 'word_cloud'),
                        ]
                    )
                            
                 ], className='choropleth_graph'),
                
                
                html.Div(children=[
                    dbc.Row(
                        [
                            html.Div(children=[
                                dbc.Row([
                                    dbc.Col(html.Label("This dropdown enables the user to generate three graphs for each region of England, highlighting predicted autism prevalence alongside gross mean weekly pay and population qualification levels for the local authority unit.)"
                                                       "The two options **England top 20** and **England bottom 20** enables the user to generate a graph relating to areas with the highest autism prevalence, level 4 qualifications and weekly gross wage. As well as the lowest autism prevalence, no qualification status and weekly gross wage.",
                                                       style={'color' : 'rgb(33 36 35)'}),
                                           )
                                ])
                            ], className='dropdown_text'),
                            dbc.Col(dcc.Dropdown(
                                id='graph-type',
                                placeholder = 'Select Region',
                                options = [
                                    {'label' : 'England top 20', 'value' : 'Englandtop'},
                                    {'label' : 'England bottom 20', 'value' : 'Englandbottom'},
                                    {'label' : 'East Midlands', 'value' : 'EastMidlands'},
                                    {'label' : 'West Midlands', 'value' : 'WestMidlands'},
                                    {'label' : 'East of England', 'value' : 'EastEngland'},
                                    {'label' : 'North West England', 'value' : 'NorthEast'},
                                    {'label' : 'North West England', 'value' : 'NorthWest'},
                                    {'label' : 'South East England', 'value' : 'SouthEast'},
                                    {'label' : 'South West England', 'value' : 'SouthWest'},
                                    {'label' : 'London', 'value' : 'London'},
                                    {'label' : 'Yorkshire and the Humber', 'value' : 'YorkshireHumber'},
                                ]
                            ),
                                   ),
                            
                                       
                                       
                        ]
                    )
                ], className='page_1_dropdown'),
                
                html.Div(children=[
                    dbc.Row(
                        [
                            html.Div(children=[
                                dbc.Col(dcc.Graph(
                                    id='prevalencegraph'),
                                        width = 100, lg={'size' : 12, "offset" : 0, 'order' : 'first'}
                                       ),
                                dbc.Col(dcc.Markdown(
                                    '''The graph above focuses on the predicted autism prevalence of each local authority within a region. 
                                    The **England top 20** and the **England bottom 20** options enable the user to explore changes in predicted prevalence rates from the highest and lowest prevalence areas from 2020
                                    and their changes to 2040.''' )
                                       )
                            ], className='prevalence_graph'),
                            
                            html.Div(children=[
                                dbc.Col(dcc.Graph(
                                    id='Qualificationbar'),
                                        width = 100, lg={'size' : 12, "offset" : 0,'order' : 'second'}
                                       ),
                                dbc.Col(dcc.Markdown(
                                    '''The graph above focuses on the qualification levels of each local authority within a region. 
                                    The **England top 20** option enables the user to highlight the the top 20 areas in England which have a higher percentage of residents qualified at level 4 and above. 
                                    The **England bottom 20** option enables the user to highlight the bottom 20 areas in England with a higher percentage of people with no formal qualifications.
                                    The user is still able to see all qualification levels in this graph.''' )
                                       )
                            ], className='qualification_bar'),
                            
                            html.Div(children=[
                                dbc.Col(dcc.Graph(
                                    id='wagegraph'),
                                        width = 100, lg={'size' : 12, "offset" : 0,'order' : 'third'}
                                       ),
                                dbc.Col(dcc.Markdown(
                                    '''The graph above focuses on the weekly gross mean wage of each local authority within a region. 
                                    The **England top 20** option enables the user to highlight the the top 20 areas in England which have a higher gross mean weekly wage. 
                                    The **England bottom 20** option enables the user to highlight the bottom 20 areas in England with a lower gross mean weekly wage.''')
                                       )  
                            ], className='wage_graph')
                        ]
                    )
                ], className= 'graph_group')
            ]
                   ),
            dcc.Tab(label = 'Tab Two', children=[
                html.Div(children=[
                    dbc.Col(dcc.Markdown(
                            '''These dropdowns allow the user to compare two locations to explore predicted autism prevalence, qualification levels and weekly gross mean income against the England mean.''')
                               ),
                    html.Div(children=[
                        dbc.Col(dcc.Dropdown(
                            id='pie_dropdown_area',
                            options=[{'label' : y, 'value' : y} for y in years],
                            value = years[0],
                            multi = False,
                            clearable = False,
                            style = {"width" : "100%"}
                        )
                               ),
                        dbc.Col(dcc.Dropdown(
                            id= 'pie_dropdown_year',
                            options = [{'label' : y, 'value' : y} for y in years2],
                            value = years2[0],
                            multi = False,
                            clearable = False,
                            style = {"width" : "100%", }
                        )
                                )
                    ], className = 'drop_one'),
                
                    html.Div(children=[
                        
                        dbc.Col(dcc.Dropdown(
                            id='pie_dropdown_area2',
                            options = [{'label' : y, 'value' : y} for y in years],
                            value = years[0],
                            multi = False,
                            clearable = False,
                            style = {"width" : "100%"}
                        )
                                ),
                        dbc.Col(dcc.Dropdown(
                            id= 'pie_dropdown_year2',
                            options = [{'label' : y, 'value' : y} for y in years2],
                            value = years2[0],
                            multi = False,
                            clearable = False, 
                            style = {"width" : "100%", }
                        )
                                )
                    ], className = 'drop_two'),
                
                    html.Div(children=[
                    
                        html.Div(children=[
                            dcc.Markdown(
                                '''The graphs below allow the user to see the weekly gross mean wage of a local authority. The red line on the indicator graph highlights the England weekly gross mean wage.
                                This enables the user to explore the deviation from this mean, while comparing to another local authority.'''),
                            dcc.Graph(id='pie_graph_indicator_wage', style = {'display' : 'inline-block', "width" : "50%"}),
                            dcc.Graph(id='pie_graph_indicator_wage2' , style = {'display' : 'inline-block', "width" : "50%"}),
                        ], className = 'pie_indicator_Wage'),
                    
                        html.Div(children=[
                            dcc.Markdown(
                                '''The graphs below focus on the predicted percentage of autistic adults within the population of a local authority.'''), 
                            dcc.Graph(id= 'pie_graph_indicator_prevalence', style = {'display' : 'inline-block', "width" : "50%"}),
                            dcc.Graph(id= 'pie_graph_indicator_prevalence2', style = {'display' : 'inline-block', "width" : "50%"}),
                        ], className = 'pie_indicator_prevalence'),
                
                        html.Div(children=[
                            dcc.Markdown(
                                '''The graphs below allow the display a pie chart showing the distribution of qualification types within the population of a local authority.'''),
                            dcc.Graph(id='pie_graph_qualification', style={'display': 'inline-block', "width" : "50%"}),
                            dcc.Graph(id='pie_graph_qualification2', style={'display':'inline-block', "width" : "50%"}),
                        ], className = 'pie_indicator_qualification'),
                    ], className = 'graphs_page_two')
                ], className = 'page_two')
            ]
                   )
        ]
                )
    ])
])
                                    
    


# In[13]:


# Autism prevalence bar graphs with timeframe slider
@app.callback(
    Output('prevalencegraph', 'figure'),
    [Input('graph-type', 'value')]
)
def choose_graph_type(graph_type):
    if graph_type is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type == 'Englandbottom':
        return px.bar(bottom20prev, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.0],hover_name="lau115nm",  title = '20 Lowest areas of predicted autism prevalence in England of 2020 and their subsequent changes until 2040',
                  width=1060,
                  height=600,
                  )
    elif graph_type == 'Englandtop':
        return px.bar(top20prev, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.8, 2.0],hover_name="lau115nm",  title = '20 Highest areas of predicted autism prevalence in England of 2020 and their subsequent changes until 2040',
                  width=1060,
                  height=600,
                  )
    elif graph_type == 'EastMidlands':
        return px.bar(eastmidlands, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.13],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the East Midlands',
                  width=1060,
                  height=600,
                  )
    elif graph_type == 'WestMidlands':
        return px.bar(westmidlands, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.25],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the West Midlands', width=1060,
                  height=600,)
    elif graph_type == 'EastEngland':
        return px.bar(eastengland, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.13],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the East of England', width=1060,
                  height=600,)
    elif graph_type == 'NorthEast':
        return px.bar(northeast, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.13],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the North East of England', width=1060,
                  height=600,)
    elif graph_type == 'NorthWest':
        return px.bar(northwest, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.13],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the North West of England', width=1060,
                  height=600,)
    elif graph_type == 'SouthEast':
        return px.bar(southeast, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.5],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the South East of England', width=1060,
                  height=600,)
    elif graph_type == 'SouthWest':
        return px.bar(southwest, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 2.0],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the South West of England', width=1060,
                  height=600,)
    elif graph_type == 'London':
        return px.bar(london, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.5],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in London', width=1060,
                  height=600,)
    elif graph_type == 'YorkshireHumber':
        return px.bar(yorkshirehumber, x='lau115nm', y='percentageprevalence', color='lau115nm', labels=dict(lau115nm="Local Authority", percentageprevalence="Percentage Prevalence"),
                     animation_frame='year', animation_group='lau115nm', range_y = [0.4, 1.13],hover_name="lau115nm",  title = 'Predicted Autism Prevalence in the Yorkshire and the Humber', width=1060,
                  height=600,)
    return None


# In[14]:


# Weekly gross mean wage bar chart
@app.callback(
    Output('wagegraph', 'figure'),
    [Input('graph-type', 'value')]
)
def choose_graph_type(graph_type):
    if graph_type is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type == 'Englandbottom':
        return px.bar(bottom20wage, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [300, 500], labels=dict(lau115nm="Local Authority")) 
    
    elif graph_type == 'Englandtop':
        return px.bar(top20wage, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [700, 1200], labels=dict(lau115nm="Local Authority"))
                     
    
    elif graph_type == 'WestMidlands':
        return px.bar(qualbarwestmids, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [300, 800], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'EastEngland':
        return px.bar(qualbareastengland, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [300, 950], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'NorthEast':
        return px.bar(qualbarnortheast, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [300, 650], labels=dict(lau115nm="Local Authority"))
       
    elif graph_type == 'EastMidlands':
        return px.bar(qualbareastmid, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060, height=600, color='lau115nm', range_y = [300, 700], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'SouthEast':
        return px.bar(qualbarsoutheast, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060, height=600, color='lau115nm', range_y = [300, 900], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'SouthWest':
        return px.bar(qualbarsouthwest, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060, height=600, color='lau115nm', range_y = [300, 1200], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'London':
        return px.bar(qualbarlondon, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage", hover_name="lau115nm", width=1060, height=600, color='lau115nm', range_y = [300, 1200], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'YorkshireHumber':
        return px.bar(qualbaryorkshire, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060, height=600, color='lau115nm', range_y = [300, 700], labels=dict(lau115nm="Local Authority"))
    elif graph_type == 'NorthWest':
        return px.bar(qualbarnorthwest, x="lau115nm", y="weeklygrosspaymean",
                           title = "Weekly gross mean Wage",  hover_name="lau115nm", width=1060,height=600, color='lau115nm', range_y = [300, 700], labels=dict(lau115nm="Local Authority"))

        
  
    
    
    return None


# In[15]:


# Qualification levels per area bar graph
@app.callback(
    Output('Qualificationbar', 'figure'),
    [Input('graph-type', 'value')]
)
def choose_graph_type(graph_type):
    if graph_type is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type == 'Englandbottom':
        return px.bar(bottom20qual, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Bottom 20 local authorities with the highest number of reisdents without formal qualifications",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",                                                                                                                                         percentageotherqualifications="Other qualifications"
                                                                                                                                            )) 
    elif graph_type == 'Englandtop':
        return px.bar(top20qual, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Top 20 local authorities with the highest number of residents with level 4 and above qualifications",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
                     
    
    elif graph_type == 'WestMidlands':
        return px.bar(qualbarwestmids, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'EastEngland':
        return px.bar(qualbareastengland, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'NorthEast':
        return px.bar(qualbarnortheast, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
       
    elif graph_type == 'EastMidlands':
        return px.bar(qualbareastmid, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060, height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'SouthEast':
        return px.bar(qualbarsoutheast, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060, height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'SouthWest':
        return px.bar(qualbarsouthwest, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060, height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'London':
        return px.bar(qualbarlondon, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage", hover_name="value", width=1060, height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'YorkshireHumber':
        return px.bar(qualbaryorkshire, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060, height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
    elif graph_type == 'NorthWest':
        return px.bar(qualbarnorthwest, x="lau115nm", y=["Percentagenoqualification", "percentagelevel1",
                                                          "percentagelevel2", "percentageapprenticeship", "percentagelevel3",
                                                          "percentagelevel4andabove", "percentageotherqualifications"],
                           title = "Qualification level by percentage",  hover_name="value", width=1060,height=600, labels=dict(lau115nm="Local Authority", Percentagenoqualification="No Qualifications", 
                                                                                                                                             percentagelevel1="Level 1 qualification", percentagelevel2="Level 2 qualification",
                                                                                                                                             percentageapprenticeship="Apprenticeship", percentagelevel3="Level 3 qualification",
                                                                                                                                             percentagelevel4andabove="Level 4 and above qualification",
                                                                                                                                             percentageotherqualifications="Other qualifications"
                                                                                                                                            ))
        
      
    
    
    return None


# In[16]:


print(pie_melt_select)
pie_filtered = pie_melt_select.iat[0,1]


# In[17]:


# Creating a pie chart for percentage of qualifications held by the population per area
@app.callback(
    Output(component_id='pie_graph_qualification', component_property='figure'),
    [Input(component_id='pie_dropdown_area', component_property='value')]
)
def update_graph(year):
    piechart_qual = px.pie(pie_melt_select[pie_melt_select['lau115nm'] == str(year)],
                   title=f"Qualification type per percentage of the population",
                   values="valuepie",
                   height=350,
                   color="namepie",
                   names="namepie",
                
                  )

    
    return piechart_qual
        
        
                     


# In[18]:


# Creating a pie chart for percentage of qualifications held by the population per area
@app.callback(
    Output(component_id='pie_graph_qualification2', component_property='figure'),
    [Input(component_id='pie_dropdown_area2', component_property='value')]
)
def update_graph(year):
    piechart_qual = px.pie(pie_melt_select[pie_melt_select['lau115nm'] == str(year)],
                   title=f"Qualification type per percentage of the population",
                   values="valuepie",
                   height=350,
                   color="namepie", 
                   names="namepie"
                  )

    
    return piechart_qual
        


# In[19]:


@app.callback(
    Output(component_id='pie_graph_indicator_wage', component_property='figure'),
    [Input(component_id='pie_dropdown_area', component_property='value')]
)
def update_graph(value):
    indicator = df.query("lau115nm == @value")["weeklygrosspaymean"].values[0]
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = indicator,
    mode = "gauge+number+delta",
    title = {'text': "Gross Weekly Mean Wage"},
    number = {'prefix': "£"},
    delta = {'reference': 585.4},
    gauge = {'axis': {'range': [None, 1187.6]},
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 585.4}}))
    fig.update_layout(
        height=250)
    

    
    return fig


# In[20]:


@app.callback(
    Output(component_id='pie_graph_indicator_wage2', component_property='figure'),
    [Input(component_id='pie_dropdown_area2', component_property='value')]
)
def update_graph(value):
    indicator = df.query("lau115nm == @value")["weeklygrosspaymean"].values[0]
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = indicator,
    mode = "gauge+number+delta",
    title = {'text': "Gross Weekly Mean Wage"},
    number = {'prefix': "£"},
    delta = {'reference': 585.4},
    gauge = {'axis': {'range': [None, 1187.6]},
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 585.4}}))
    fig.update_layout(
        height=250
    )

    
    return fig


# In[21]:


@app.callback(
    Output(component_id='pie_graph_indicator_prevalence', component_property='figure'),
    [Input(component_id='pie_dropdown_area', component_property='value'),
    Input(component_id='pie_dropdown_year', component_property='value')]
)
def update_graph(value, year):
    indicator2 = df.query("lau115nm == @value & year == @year")["percentageprevalence"].values[0]
    fig = go.Figure(go.Indicator(
        mode = "number+delta",
        value = indicator2,
        number = {'prefix': "%"},
        delta = {'position': "top", 'reference': 100},
        domain = {'x': [0, 1], 'y': [0, 1]}))
    
    fig.update_layout(
    height=250,
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Percentage of Autism Prevalence of Population Per Area"},
        'mode' : "number+gauge"
        }]
                         }})
    return fig


# In[22]:


@app.callback(
    Output(component_id='pie_graph_indicator_prevalence2', component_property='figure'),
    [Input(component_id='pie_dropdown_area2', component_property='value'),
    Input(component_id='pie_dropdown_year2', component_property='value')]
)
def update_graph(value, year):
    indicator2 = df.query("lau115nm == @value & year == @year")["percentageprevalence"].values[0]
    fig = go.Figure(go.Indicator(
        mode = "number+delta",
        value = indicator2, 
        number = {'prefix': "%"},
        delta = {'position': "top", 'reference': 100},
        domain = {'x': [0, 1], 'y': [0, 1]}))
    
    fig.update_layout(
    height=250,
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Percentage of Autism Prevalence of Population Per Area"},
        'mode' : "number+gauge"
        }]
                         }})
    return fig


# In[25]:


if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




