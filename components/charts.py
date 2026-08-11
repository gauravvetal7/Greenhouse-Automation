import plotly.graph_objects as go

def create_chart(title, values, color):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=values,
            mode="lines+markers",
            line=dict(color=color, width=3),
            marker=dict(size=6)
        )
    )

    fig.update_layout(
        title=title,
        height=300,
        template="plotly_dark",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis_title="Time",
        yaxis_title=title,
        showlegend=False
    )

    return fig