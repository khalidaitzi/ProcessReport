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
  
  # Remove table centering
  st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

  # Add some padding 
  st.markdown("""
    <style>
      .st-bo {
        padding: 20px;  
        margin-left: -400px;
        .full-width-table th {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
      }
    </style>    
    """, unsafe_allow_html=True)

cw1, cw2 = st.columns((2.5, 1.7))
                    
for i in range(0,9):
        colourcode.append(df['c'+str(i)].tolist())   
    
    df = df[['executionId', 'account', 'executionTime', 'status', 'executionType', 'processName', 'processId', 'atomName', 'atomId', 'inboundDocumentCount', 'inboundErrorDocumentCount', 'outboundDocumentCount', 'executionDuration', 'inboundDocumentSize', 'outboundDocumentSize', 'nodeId',
]]
    
       
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], columnwidth = [30,10,10,10,10,15,15,15,15,15],
                header = dict(
                 values = list(df.columns),
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              , cells = dict(
                  values = [df[K].tolist() for K in df.columns], 
                  font=dict(size=12),
                  align = ['left','center'],
                  fill_color = colourcode,
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])
     
    fig.update_layout(title_text="Current Waiting Handovers",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)                                                           
        
    cw1.plotly_chart(fig, use_container_width=True)    

  
  # Render as full width table
  st.markdown(f'<div class="st-bo"><table class="full-width-table">{df.to_html(index=False)}</table></div>', unsafe_allow_html=True)
