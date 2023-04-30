import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('heartRateZones.csv')


df_pivoted = df.pivot(index=['date'], columns='name', values='caloriesOut')
df_pivoted.columns = [col for col in df_pivoted.columns.values]
df_pivoted.reset_index(inplace=True)

st.line_chart(df_pivoted, x = 'date')

df_new = df.groupby('name').agg({'min': 'min', 'max': 'max'})
df_new = df_new.reset_index()
st.write(df_new)