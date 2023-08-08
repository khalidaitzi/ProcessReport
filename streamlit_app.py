import streamlit as st
import requests
import pandas as pd
import xml.etree.ElementTree as ET

username = 'ait-zi.khalid@ensam-casa.ma'
password = '$2"5EVTtb,D3xUN'

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
    
    # Set CSS styling to align the table to the left
    st.markdown(
        """
        <style>
        .dataframe {
            margin-left: -100;
            margin-right: 100;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.table(df)
