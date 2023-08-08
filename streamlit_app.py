import streamlit as st
import requests

username = 'ait-zi.khalid@ensam-casa.ma'
password = '$2"5EVTtb,D3xUN'

def get_data():
    url = 'https://api.boomi.com/api/rest/v1/trainingkhalidaitzi-K6LQT4/ExecutionRecord/query'
    response = requests.get(url, auth=(username, password))
    return response.text

if __name__ == '__main__':
    data = get_data()
    st.write(data)
