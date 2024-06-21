import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.title('How to avoid DeReLiCT Code')

st.write("Basic steps to help avoid total code collapse.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["De", "Re", "Li", "C", "T"])

with tab1:
    st.header("Dependencies: record them!")
    
    st.write("You might hear researchers or code users complain about [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).",
             "While juggling dependencies occurs at every level of computing, we are going to focus specifically on your scientific code,",
             "and how to avoid future errors and issues with reproducibility by recording your dependencies.")
    st.write("Regardless of the language you are using to write your scientific research code, there will be different versions of the language itself,",
             "and different versions of the plug-ins and libraries you use.")
    # https://lp.jetbrains.com/python-developers-survey-2022/
    # Copyright © JetBrains s.r.o. 2023
    # cc-by-4.0
    where_dependencies = {
        
        "requirements.txt" : 69,
        "pyproject.toml": 33,
        "poetry.lock": 25,
        "pipfile.lock": 15,
        "Conda environment.yml": 11,
        "pip constraints.txt": 6,
        "Other": 4,
        "None": 4,
    }

    tools_for_dependencies = {
        "poetry": 30,
        "pipenv": 28,
        "pip-tools": 26,
        "Other" : 4,
        "None": 28,
    }


    df_where_dep = pd.DataFrame.from_dict(where_dependencies, orient='index', columns=["Percentage"]).sort_values("Percentage").reset_index()
    df_tools = pd.DataFrame.from_dict(tools_for_dependencies, orient='index', columns=["Percentage"]).sort_values("Percentage").reset_index()


    st.subheader('What format is your application dependency information stored in?')
    st.write("Responders could select more than one option. The total may be greater than 100% for this multiple-answer question.")
    st.write("*Data from Python developers survey 2022. Copyright © JetBrains s.r.o. 2023.*")
    st.altair_chart(
        alt.Chart(df_where_dep).mark_bar(
            size=40,
            cornerRadiusBottomRight=3,
            cornerRadiusTopRight=3
            ).encode(
        y=alt.Y('index').sort('-x'),
        x='Percentage',
        color=alt.Color("Percentage", legend=None).scale(scheme="bluepurple")).properties(height=alt.Step(50)).configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_axisY(labelAlign="right", labelLimit=300, title=None),
        use_container_width=True,
        
    )

    st.subheader('Which tools do you use for application dependency management?')
    st.write("Responders could select more than one option. The total may be greater than 100% for this multiple-answer question.")
    st.write("*Data from Python developers survey 2022. Copyright © JetBrains s.r.o. 2023.*")
    st.altair_chart(
        alt.Chart(df_tools).mark_bar(
            size=40,
            cornerRadiusBottomRight=3,
            cornerRadiusTopRight=3
            ).encode(
        y=alt.Y('index').sort('-x'),
        x='Percentage',
        color=alt.Color("Percentage", legend=None).scale(scheme="bluepurple")).properties(height=alt.Step(50)).configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_axisY(labelAlign="right", labelLimit=300, title=None),
        use_container_width=True,
        
    )

with tab2:
    st.write("Tab 2")
    
