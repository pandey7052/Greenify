import plotly.express as px


def getResourceByType(df, type='Urban Utility'):
    return px.bar(df, x=type, y='State', color='State',
                  title='Energy Usage in urban area', height=600)
