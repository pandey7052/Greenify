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


def getLocationData(df, state, cols, title=""):
    data = df[df['State'] == state][cols].T
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))


def getCountryNum(df):
    data = df.groupby('location').count()
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data['type'].values.flatten()))


def getCountryValue(df):
    data = df['Daily MWh ']
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=df.location, y=data.values.flatten()))


def getCountryType(df):
    data = df.groupby('type').count()['name']
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))


def getTotalEmission(df):
    df['Total'] = df.sum(axis=1)
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=df.Country, y=df.values.flatten()))


def getEmissionByCountry(df, con):
    years = list(map(str, range(1970, 2021)))
    data = df[df['Country'] == con][years].T
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))


def getEmissionByYear(df, year):
    data = df.set_index('Country')[year]
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))


def getTopEmissionByYear(df, year):
    data = df.set_index('Country')[year].sort_values(ascending=False).head(10)
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))


def getBottomEmissionByYear(df, year):
    data = df.set_index('Country')[year].sort_values().head(10)
    fig = go.Figure()
    return fig.add_trace(go.Bar(x=data.index, y=data.values.flatten()))
