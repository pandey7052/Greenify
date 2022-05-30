import streamlit as st
import pandas as pd
# import json
# import geopandas as gpd

from visualizer import getResourceByType, getResourceByLocation, getLocationData

sidebar = st.sidebar
st.title('GREENIFY')
st.image('greenify.jpg.png')
st.subheader('Analysis of World Energy & Electricity Resources')


# @st.cache(suppress_st_warning=True)
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


df = loadData('datasets/usretechnicalpotential.csv')
df = cleanData(df)
# st.dataframe(df)


def overview():
    # st.image('imh.jpg')
    # st.image('climate.jpeg')

    st.markdown('''### Energy is an important ingredient in all phases of society. We live in a very interdependent world, and access to adequate and reliable energy resources is crucial for economic growth and for maintaining the quality of our lives. But current levels of energy consumption and production are not sustainable.
    ''')
    st.header('Project Introduction')
    st.markdown('''### 	This project titled “Analysis of World Energy and Electricity Resources” focuses on the data obtained about energy resources utilized, energy and electricity wastage globally. 
    ''')

    # st.header('Objective')
    ##st.subheader(' To deal with the following situations :')
    ##st.subheader(' Climate Change  :')
    # st.image('climate-change2.jpg')
    # st.markdown(''' Understanding and Predicting the global atmospheric and climate change .
    # ''')
    ##st.subheader(' Global Warming :')
    # st.image('CG.jpg')
    # st.markdown('''   To increase the understanding of the atmosphere/ecosystem exchange of greenhouse gasses .
    # ''')
    ##st.subheader('Temperature Analysis :')
    # st.image('temperatureanalysis.jpg')
    ##st.subheader('Determine the Energy Usage :')
    st.header('Purpose And Scope :-')
   
    c1, c2 = st.columns(2)
    c2.subheader(' Analyze the Data :')
    st.markdown('#')
    c1.image('cg2.jpg')

    c1, c2 = st.columns(2)
    c2.subheader(' Determine the Energy Usage:')
    st.markdown('#')
    c1.image('cg1.jpg')

    c1, c2 = st.columns(2)
    c2.subheader(' Reduction of Energy Waste :')
    st.markdown('#')
    c1.image('Reduction of Energy Waste.jpg')

    c1, c2 = st.columns(2)
    c2.subheader(' Increase dependency on Renewable Sources :')
    st.markdown('#')
    c1.image('Renewal-energy.jpg')

    #st.markdown(
       # '''  Specific analysis of the impact of selected climatic scenarios on Exchange of temperature . ''')
    st.header('Conclusion :-')
    st.markdown(''' This project sends a valuable message backed by Science and its tools to keep our resources in check and direct a sustainable usage.

    ''')
    st.markdown(''' Energy is a valuable resource which should be used efficiently and never be wasted.
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
    dataframe = df

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.columns(4)
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
            cols = st.columns(4)
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
    st.plotly_chart(getResourceByType(
        df, 'Urban Utility'), use_container_width=True)

    st.markdown('#')
    st.subheader('Solar Thermal')
    st.plotly_chart(getResourceByType(
        df, 'Solar Thermal'), use_container_width=True)

    st.markdown('#')
    st.subheader('Onshore Wind')
    st.plotly_chart(getResourceByType(
        df, 'Onshore Wind'), use_container_width=True)

    st.markdown('#')
    st.subheader('Offshore Wind')
    st.plotly_chart(getResourceByType(
        df, 'Offshore Wind'), use_container_width=True)

    st.markdown('#')
    st.subheader('Bio-Solid')
    st.plotly_chart(getResourceByType(
        df, 'Bio-Solid'), use_container_width=True)


def locationAnalysis():
    st.header('Location Analysis')
    st.markdown('---')
    states = df.State.unique()
    selState = st.selectbox('Select State', states)
    colSet = [
        ['Solar Photovoltic', 'Solar Thermal'],
        ['Onshore Wind', 'Offshore Wind'],
        ['Bio-Solid', 'Bio-gas', 'Bio-CH4'],
        ['Urban Utility', 'Rural Utility'],
    ]
    for col in colSet:
        st.subheader(f'Energy Sources from {selState}')
        st.plotly_chart(getLocationData(df=df, state=selState, cols=col,
                        title=""), use_container_width=True)
        st.markdown('#')


def locationAnalysis2():
    st.markdown('''
        ## Energy Source Location Analysis
        ---
    ''')

    st.markdown('#')
    st.subheader('Solar Photovoltic')
    st.plotly_chart(getResourceByLocation(
        df, y_col='Bio-Solid'), use_container_width=True)
    st.markdown('#')
    st.subheader('Bio Gas')
    st.plotly_chart(getResourceByLocation(
        df, y_col='Bio-gas'), use_container_width=True)
    st.markdown('#')
    st.subheader('Hydro Power')
    st.plotly_chart(getResourceByLocation(
        df, y_col='Hydropower'), use_container_width=True)
    st.markdown('#')
    st.subheader('Hydropower Sites Count')
    st.plotly_chart(getResourceByLocation(
        df, y_col='Hydropower Sites Count'), use_container_width=True)


def carbonAnalysis():
    st.header('Footpint Analysis')


def categoryAnalysis():
    st.header('Category Analysis')


sidebar.header('Choose Your Option')
options = ['Project Overview', 'Dataset Details', 'Location and category Analysis', 'Type Analysis']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    overview()
elif choice == options[1]:
    viewDataset()
elif choice == options[2]:
    locationAnalysis()
elif choice == options[3]:
    sourceTypeAnalysis()
elif choice == options[4]:
    categoryAnalysis()
elif choice == options[5]:
    sourceTypeAnalysis()
elif choice == options[6]:
    sourceTypeAnalysis()
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
