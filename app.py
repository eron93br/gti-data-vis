import numpy as np
import pandas as pd
import streamlit as st
from common import stream_data, load_tips_dataset, make_visualization1
import plotly.express as px

with st.sidebar:
    st.write("Sidebar")

with st.container():
    st.title("Dashboard GTI")
    st.image("assets/image.png")
    df = load_tips_dataset()
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.write("---- Dashboard GTI 2025 -----")
    
    st.header("Histograma da Gorjeta (tip)")
    fig = make_visualization1(df)
    st.plotly_chart(fig)
    

    st.header("Detalhamento do Prompt")

    st.write("Dashboard GTI 2025")

    if st.button("Stream data"):
        st.write_stream(stream_data)