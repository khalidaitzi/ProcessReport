import streamlit as st
import requests
import pandas as pd
import xml.etree.ElementTree as ET

username = 'ait-zi.khalid@ensam-casa.ma'
password = '$2"5EVTtb,D3xUN'

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
    url = 'https://api.boomi.com/api/rest/v1/trainingkhalidaitzi-K6LQT4/ExecutionRecord/query'
    response = requests.post(url, auth=(username, password))
    return response.text

if __name__ == '__main__':
    data = get_data()
    records = parse_xml_response(data)
    df = pd.DataFrame(records)

    # Add some padding to the container
    st.markdown("""
        <style>
            .stContainer {
                padding: 20px;
            }
        </style>
        """, unsafe_allow_html=True)

    # Add margin-left to the title
    st.markdown("""
        <style>
            .title-wrapper {
                margin-left: 6500px;
            }
        </style>
        """, unsafe_allow_html=True)

    # Decorate the table with colors
    st.markdown("""
        <style>
            .full-width-table {
                width: 100%;
                border-collapse: collapse;
            }
            .full-width-table th {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            .full-width-table td {
                border: 1px solid #ddd;
                padding: 8px;
            }
        </style>
        """, unsafe_allow_html=True)

    # Render the title and table
    st.title(":clipboard: Process reporting")
    st.table(df.style.set_table_attributes("class='full-width-table'"))
