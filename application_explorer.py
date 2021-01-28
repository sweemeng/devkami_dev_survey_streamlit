import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
from utils import *


st.title('DevKami Malaysian Developer Survey: Application')

df = load_data("devkami_survey.tsv")

supported_fields = {
    'Application Type': 'application_built',
    'Language Used': 'language_used',
    'OS Deployed': 'os_deployed',
    'OS Used': 'os_coded',
    'IDE': 'ide_used',
    'Version Control': 'vcs_used',
    'Issue Tracker': 'tracker_used',
}

field = st.selectbox(
    'Select Field',
     list(supported_fields.keys()),
     )

st.header("General stats")

counter = count_cols(df[supported_fields[field]])
fig, ax = plt.subplots()
generate_hbar_subplot(counter.keys(), counter.values(), 'Usage Count', field, field, ax)

st.pyplot(fig)
st.header("Specific stats")
option = st.selectbox(f'Select {field}', get_nested_values(df[supported_fields[field]]))

has_value = filter_by_field(supported_fields[field], df, option)
new_df = df[has_value]
lang_counter = count_cols(new_df['language_used'])
ide_counter = count_cols(new_df['ide_used'])
os_used_counter = count_cols(new_df['os_coded'])
os_deployed_counter = count_cols(new_df['os_deployed'])
app_counter = count_cols(new_df['application_built'])
tracker_counter = count_cols(new_df['tracker_used'])
vcs_counter = count_cols(new_df['vcs_used'])

fig, ax = plt.subplots()
generate_hbar_subplot(
        lang_counter.keys(), 
        lang_counter.values(), 
        'Usage', 
        'Programming Language', 
        'Programming Language',
        ax
)
st.pyplot(fig)

fig, ax = plt.subplots()
generate_hbar_subplot(
        app_counter.keys(), 
        app_counter.values(), 
        'Count', 
        'Application', 
        'Application',
        ax
)
st.pyplot(fig)


fig, ax = plt.subplots()
generate_hbar_subplot(
        ide_counter.keys(), 
        ide_counter.values(), 
        'Usage', 
        'IDE used', 
        'IDE',
        ax
)

st.pyplot(fig)

fig, ax = plt.subplots()
generate_hbar_subplot(
        os_used_counter.keys(), 
        os_used_counter.values(), 
        'Usage', 
        'OS used', 
        'OS',
        ax
)

st.pyplot(fig)

fig, ax = plt.subplots()
generate_hbar_subplot(
        os_deployed_counter.keys(), 
        os_deployed_counter.values(), 
        'Usage', 
        'OS deployed', 
        'OS',
        ax
)

st.pyplot(fig)

fig, ax = plt.subplots()
generate_hbar_subplot(
        vcs_counter.keys(), 
        vcs_counter.values(), 
        'Usage', 
        'VCS deployed', 
        'VCS',
        ax
)

st.pyplot(fig)

fig, ax = plt.subplots()
generate_hbar_subplot(
        tracker_counter.keys(), 
        tracker_counter.values(), 
        'Usage', 
        'Issue Tracker', 
        'Issue Tracker',
        ax
)

st.pyplot(fig)

