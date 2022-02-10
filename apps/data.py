import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():

    # 001. Title
    st.title('Explore a dataset')
    st.write('A general purpose data exploration app')

    # 002. Upload FILES
    files = st.file_uploader("Upload file",accept_multiple_files=True, type=['csv'])
    
    # 003. Dataframe
    for i in files:
        a = i.name
        a = a[len(a)-6:-4]

        df = pd.read_csv(i, encoding='CP949',skiprows=3)
        
        Enc_mec = df['Enc_Mec']

        dt=0
        new_list = []

        new_list.append(Enc_mec[0])
        for i in range(1,len(Enc_mec)+1):
            if i == len(Enc_mec):
                break
            elif Enc_mec[i-1]>Enc_mec[i]:
                dt +=1
                new_list.append(Enc_mec[i]+360*dt)
            else:
                new_list.append(Enc_mec[i]+360*dt)

        df['New_Enc_Mec']= new_list

        df1 = df.drop_duplicates('New_Enc_Mec')
        
        st.write(df1)
