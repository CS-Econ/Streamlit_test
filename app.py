import streamlit as st
import plotly.express as px

st.header('Streamlit test')
fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 9, 16], title='test title')
fig.update_layout(
    xaxis_title='test',
    yaxis_title='&mu;g/m<sup>2</sup>'
)

st.plotly_chart(fig)
