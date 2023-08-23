import streamlit as st
import requests 
import pandas as pd
import xml.etree.ElementTree as ET
import plotly.graph_objects as go

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

    cw1, cw2 = st.columns((2.5, 1.7))

    colourcode = []

    for i in range(0, 16):
        column_name = 'c' + str(i)
        if column_name in df.columns:
            colourcode.append(df[column_name].tolist())
        else:
            st.warning(f"Column '{column_name}' does not exist in the DataFrame.")

    df = df[['executionId', 'account', 'executionTime', 'status', 'executionType', 'processName', 'processId', 'atomName', 'atomId', 'inboundDocumentCount', 'inboundErrorDocumentCount', 'outboundDocumentCount', 'executionDuration', 'inboundDocumentSize', 'outboundDocumentSize', 'nodeId']]

    fig = go.Figure(
        data=[go.Table(
            columnorder=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            columnwidth=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
            columnheight=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
            header=dict(
                values=list(df.columns),
                font=dict(size=12, color='white'),
                fill_color='#264653',
                line_color='rgba(255,255,255,0.2)',
                align=[ 'center'],
                height=100
            ),
            cells=dict(
                values=[df[K].tolist() for K in df.columns], 
                font=dict(size=12),
                align=[ 'center'],
                fill_color=colourcode,
                line_color='rgba(255,255,255,0.2)',
                height=100
            )
        )]
    )

    fig.update_layout(
        title_font_color='#264653',
        title_x=0,
        margin=dict(l=0, r=10, b=10, t=30),
        height=600
    )

    cw1.plotly_chart(fig, use_container_width=True)

