import plotly.graph_objects as go
import streamlit as st


def create_gauge(title, value, min_value=0, max_value=100, unit=""):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            number={"suffix": unit},
            gauge={
                "axis": {
                    "range": [min_value, max_value]
                },
                "bar": {
                    "thickness": 0.7
                },
                "steps": [
                    {
                        "range": [min_value, max_value],
                    }
                ],
            },
        )
    )

    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, width="stretch")