import streamlit as st
import requests
from xml.etree import ElementTree

username = 'ait-zi.khalid@ensam-casa.ma'
password = '$2"5EVTtb,D3xUN'

def get_data():
    url = 'https://api.boomi.com/api/rest/v1/trainingkhalidaitzi-K6LQT4/ExecutionRecord/query'
    response = requests.post(url, auth=(username, password))  
    return response.text

def parse_xml(xml):
    root = ElementTree.fromstring(xml)
    results = []
    for result in root.findall('bns:result', root.nsmap):
         data = []
         for child in result:
             data.append(child.text)
         results.append(data)
    return results

if __name__ == '__main__':
    data = get_data()    
    results = parse_xml(data) 
    st.table(results)
