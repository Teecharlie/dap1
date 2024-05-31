import streamlit as st
import pandas as pd
import plotly.express as px


def formatIndex(df):
    df['S/No.'] = range(1, len(df) + 1)
    df = df.set_index('S/No.')
    return df

df=pd.read_csv('superstore.csv',encoding='latin1')
#st.write(df.head())
#get a list of products
product_list=df['Product Name'].unique()
total_sales_products=df[['Product Name','Sales']].groupby('Product Name').agg({'Sales':'sum'}).reset_index().sort_values(by='Sales',ascending=False)
total_sales_products['Sales']=round(total_sales_products['Sales'],2)
total_sales_products=formatIndex(total_sales_products)
st.dataframe(total_sales_products.head(10))