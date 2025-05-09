import numpy as np
import pandas as pd
import streamlit as st
from common import stream_data, load_tips_dataset, make_visualization1, make_visualization2
import plotly.express as px

with st.sidebar:
    st.write("Sidebar")
    _, scol2, _ = st.columns(3)
    with scol2:
        st.image("assets/cesar.png")
    sel_radio = st.radio(
        "Escolha uma opção:",
        ("Boxplot em pé", "Boxplot deitado")
    )
    print(f"Foi escolhido {sel_radio}")

with st.container():
    st.title("Dashboard GTI")
    st.image("assets/image.png")
    df = load_tips_dataset()
    st.write(df.head(3))
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.write("---- Dashboard GTI 2025 -----")
    
    # ------------- FIGURA HISTOGRAMA -----------
    st.header("Histograma da Gorjeta (tip)")
    ccol1, ccol2 = st.columns(2)
    with ccol1:
        fig1 = make_visualization1(df)
        st.plotly_chart(fig1)
    
    with ccol2:
        fig2 = make_visualization2(df, sel_radio)
        st.plotly_chart(fig2)

    # -------------------------------------------------

    st.header("Detalhamento do Prompt")

    st.write("Dashboard GTI 2025")

    if st.button("Stream data"):
        st.write_stream(stream_data)