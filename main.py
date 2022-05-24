import streamlit as st
import pandas as pd

sidebar = st.sidebar
st.title('Greenify')
st.subheader('Analysis of World Energy & Electricity Resources')

# load data here


@st.cache(suppress_st_warning=True)
def loadData(path):
    return pd.read_csv(path)


def cleanData(df):
    df = df.drop(['urbanUtilityScalePV_GW', 'urbanUtilityScalePV_km2', 'ruralUtilityScalePV_GW',
                  'ruralUtilityScalePV_km2', 'rooftopPV_GW', 'CSP_GW', 'CSP_km2', 'onshoreWind_GW',
                  'onshoreWind_km2', 'offshoreWind_GW', 'offshoreWind_km2', 'biopowerSolid_GW',
                  'biopowerSolid_BDT', 'biopowerGaseous_GW', 'geothermalHydrothermal_GW', 'EGSGeothermal_GW',
                  'hydropower_GW'], axis=1)
    return df.rename({'Unnamed: 0': 'State', 'urbanUtilityScalePV_GWh': 'Urban Utility',
                      'ruralUtilityScalePV_GWh': 'Rural Utility', 'rooftopPV_GWh': 'Solar Photovoltic',
                      'CSP_GWh': 'Solar Thermal', 'onshoreWind_GWh': 'Onshore Wind', 'offshoreWind_GWh': 'Offshore Wind',
                      'biopowerSolid_GWh': 'Bio-Solid', 'biopowerGaseous_GWh': 'Bio-gas', 'biopowerGaseous_Tonnes-CH4': 'Bio-CH4',
                      'geothermalHydrothermal_GWh': 'Hydrothermal', 'EGSGeothermal_GWh': 'Enhanced Geothermal',
                      'hydropower_GWh': 'Hydropower', 'hydropower_countOfSites': 'Hydropower Sites Count'}, axis=1)


def overview():

    # st.image('climate.jpeg')

    st.markdown('''### Global warming is the increase of average world temperatures as a result of what is known as the greenhouse effect.
    As the greenhouse gases build up in the atmosphere the Earth gets hotter.
    This process is leading to a rapid change in climate, also known as climate change.
    ''')
    st.header('Project Introduction')
    st.markdown('''### In this project we have been to create models of how changes caused by heating should work their way through the entire system and appear in different areas, for example, Sea Level, Flood,Extreme Weather,Volcanic Activity etc .
    ''')
    st.image('global_warming.jpg')
    st.header('Objective')
    st.subheader(' Earth Observation :')
    st.markdown(''' Understanding and Predicting the global atmospheric and climate change .
    ''')
    st.subheader(' Climate Impact :')
    st.markdown('''   To increase the understanding of the atmosphere/ecosystem exchange of greenhouse gasses .
    ''')
    st.subheader('Temperature Analysis :')
    st.markdown(
        '''  Specific analysis of the impact of selected climatic scenarios on Exchange of temperature . ''')
    st.header('Conclusion')
    st.markdown(''' ### The project will contribute to an improved understanding of the processes, and also use the knowledge gained to make an estimate of the contribution from the natural ecosystems to the emissions of greenhouse gasses .
    ''')
    st.markdown(''' ### Human-induced climate change has contributed to changing patterns of extreme weather across the globe, from longer and hotter heat waves to heavier rains. Extreme weather is on the rise, and the indications are that it will continue to increase, in both predictable and unpredictable ways.
    ''')


def generateReport():
    sidebar.header("Save Report")
    current_report['title'] = sidebar.text_input('Report Title')
    current_report['desc'] = sidebar.text_input('Report Description')
    current_report['img_name'] = sidebar.text_input('Image Name')
    current_report['save_report'] = sidebar.button("Save Report")


def save_report_form(fig):
    generateReport()
    if current_report['save_report']:
        with st.spinner("Saving Report..."):
            try:
                path = 'reports/'+current_report['img_name']+'.png'
                fig.write_image(path)
                report = Report(
                    title=current_report['title'], desc=current_report['desc'], img_name=path)
                sess.add(report)
                sess.commit()
                st.success('Report Saved')
            except Exception as e:
                st.error('Something went Wrong')
                print(e)


def viewDataset():
    st.header('Data Used in Project')
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def sourceTypeAnalysis():
    st.markdown('''
        ## Energy Source Type Analysis
        ---
    ''')

    st.markdown('#')
    st.subheader('Solar Photovoltic')
    st.plotly_chart()


def analyseType():
    return


sidebar.header('Choose Your Option')
options = ['Project Overview', 'Dataset Details', 'Timeline Analysis', 'Location Analysis',
           'Source Category Analysis', 'Consumption Analysis', 'Impact Analysis', 'Carbon Footprint Analysis',
           'Demand and Supply Gap Analysis']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    overview()
elif choice == options[1]:
    viewDataset()
# elif choice == options[2]:
#     analyseTemperature()
# elif choice == options[3]:
#     analyseFloods()
# elif choice == options[4]:
#     analyseDisasters()
# elif choice == options[5]:
#     analyseSeaLevel()

# elif choice == options[6]:
#     ViewReport()
