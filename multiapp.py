

from decimal import ROUND_UP
from doctest import DONT_ACCEPT_TRUE_FOR_1
import streamlit as st
import pandas as pd
import math

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
import itertools
from bokeh.palettes import Magma, Inferno, Plasma, Viridis, Cividis, Paired
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 001. Title
st.title('Resolver Data Analysis Tool')

# df0 = pd.read_csv('df0.csv',encoding='CP949',skiprows=3)
# df0['New_Enc_Mec'] = 0
# df0['Error_min'] = 0

# # 004. Dataframe print
# # st.dataframe(df1)
# column_list = df0.columns.values.tolist()
# column_list.append("none")

# default_ix = column_list.index("New_Enc_Mec")
# default_iy = column_list.index("Cos (V)")
# default_iy2 = column_list.index("Sin (V)")

# # 005. Graph setting sidebar
# # st.sidebar.title("Graph1 Settings")
# Add_graph_title = st.sidebar.text_input('Graph Title', 'Title : ')
# Add_xaxis_label = st.sidebar.text_input('Xaxis Label', 'X : Angle')
# Add_yaxis_label = st.sidebar.text_input('Yaxis Label', 'Y : Error ')

# graph1_xoption = st.sidebar.selectbox('Xaxis Data Selection',(column_list), index=default_ix)
# graph1_yoption = st.sidebar.selectbox('Yaxis Data Selection',(column_list), index=default_iy)
# graph1_y2option = st.sidebar.selectbox('Y2axis Data Selection',(column_list), index=default_iy2)

# Max_list = []
# min_list = []
# mean_list = []

# # 002. Upload FILES
# files = st.file_uploader("Upload file",accept_multiple_files=True, type=['csv'])
# fig = make_subplots(rows=1, cols=1)

# if len(files)==0:
#     st.title('Upload rawdata Files')
    
# else:
#     st.write(len(files))
#     # 003. Read data(Drop Duplicates & Add reference Angle)
    
    
#     for i in files:
#         a = i.name
#         a = a[len(a)-6:-4]

#         df = pd.read_csv(i, encoding='CP949',skiprows=3)
        
#         Enc_mec = df['Enc_Mec']

#         dt=0
#         new_list = []

#         new_list.append(Enc_mec[0])
#         for i in range(1,len(Enc_mec)+1):
#             if i == len(Enc_mec):
#                 break
#             elif Enc_mec[i-1]>Enc_mec[i]:
#                 dt +=1
#                 new_list.append(Enc_mec[i]+360*dt)
#             else:
#                 new_list.append(Enc_mec[i]+360*dt)

#         df['New_Enc_Mec']= new_list

#         df1 = df.drop_duplicates('New_Enc_Mec')
#         df1['Error_min'] = (df['Error-Mech']-df['Error-Mech'].mean())*60

#         # st.write(df1[graph1_yoption].describe()[['mean','max','min']])
#         Max_list.append(df1[graph1_yoption].max())
#         min_list.append(df1[graph1_yoption].min())
#         mean_list.append(df1[graph1_yoption].mean())

#         # 006. Plotting
#         fig.add_trace(go.Scatter(
#             x=df[graph1_xoption], 
#             y=df[graph1_yoption],
#             name=graph1_yoption,
#             legendgroup = '1')
#             , row=1, col=1)
    
# # 005-1. Check X-axis range
# if graph1_xoption == "Time (s)":
#     Xaxis_range = st.sidebar.slider('Xaxis range',
#                             int(df1[graph1_xoption].min()), int(df1[graph1_xoption].max()),
#                             (int(df1[graph1_xoption].min()), int(df1[graph1_xoption].max())))
# else:
#     Xaxis_range = st.sidebar.slider('Xaxis range',
#                                 int(df1[graph1_xoption].min()), int(df1[graph1_xoption].max()),
#                                 (int(df1[graph1_xoption].min()), int(df1[graph1_xoption].max()*0.5)))

# # 005-2. Check Y-axis range
# Y_axis_check = abs(df1[graph1_yoption].max()-df1[graph1_yoption].min())/2
# Yaxis_range = st.sidebar.slider('Yaxis range',-5, 5,(-3,3))
    
# fig.update_layout(
#     legend_tracegroupgap = 10,
#     xaxis1_range = [Xaxis_range[0], Xaxis_range[1]],
#     yaxis1_range = [Yaxis_range[0], Yaxis_range[1]],
#     )
        
# st.plotly_chart(fig, use_container_width=True)

# df2 = pd.DataFrame()

# df2['max'] = Max_list
# df2['min'] = min_list
# df2['mean'] = mean_list
# df2['Error'] = (df2['max']-df2['min'])/2
# st.write(df2)
# st.write(df1)
