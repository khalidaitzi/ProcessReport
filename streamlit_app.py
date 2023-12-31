import streamlit as st
import requests 
import pandas as pd
import xml.etree.ElementTree as ET

username = '*************'
password = '*************'

# Set Streamlit theme
st.set_page_config(
    page_title="Process reporting",
    page_icon=":clipboard:",
    layout="wide"
)

# Define custom CSS styles
custom_styles = """
<style>
    /* Remove table centering */
    div.row-widget.stRadio > div {
        flex-direction: row;
    }

    /* Add padding and margin to table */
    .dataframe {
        padding: 20px;
        margin-left: -400px;
    }

    /* Style table header */
    .dataframe th {
        background-color: #8684f0;
        border: 2px solid #ddd;
        padding: 10px;
        text-align: left;
    }

    /* Style table cells */
    .dataframe td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    /* Alternate row colors */
    .dataframe tr:nth-child(even) {
        background-color: #8684f0;
    }

    /* Hover effect on rows */
    .dataframe tr:hover {
        background-color: #8684f0;
    }
</style>
"""
st.title(":clipboard: Process reporting")
def parse_xml_response(xml_response):
    root = ET.fromstring(xml_response)
    records = []
    for result in root.findall('.//{http://api.platform.boomi.com/}result'):
        record = {}
        for child in result:
            tag = child.tag.replace('{http://api.platform.boomi.com/}', '')
            record[tag] = child.text
        records.append(record)
    return records

def get_data():
    url = 'https://api.boomi.com/api/rest/v1/*********************/ExecutionRecord/query'
    response = requests.post(url, auth=(username, password))
    return response.text

if __name__ == '__main__':
    data = get_data()
    records = parse_xml_response(data)
    df = pd.DataFrame(records)

    # Apply custom styles
    st.markdown(custom_styles, unsafe_allow_html=True)

    # Render table
    st.dataframe(df)
