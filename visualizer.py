import plotly.express as px
import plotly.graph_objs as go


def getResourceByType(df, type='Urban Utility'):
    return px.bar(df, x=type, y='State', color='State',
                  title='Energy Usage in urban area', height=600)


def getResourceByLocation(df, count=20, y_col='Bio-Solid'):
    bs_df = df.sort_values(y_col, ascending=False)
    bs_df = bs_df[:count]
    return px.bar(bs_df, x='State', y=y_col, color='State',
                  title='States with highest Bioplant-Solid Energy production',
                  labels={'x': 'State', 'y': 'Energy'})


def getLocationData(df, state, title=""):
    data = df[df['State'] == state][df.columns[3:]].T
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))
