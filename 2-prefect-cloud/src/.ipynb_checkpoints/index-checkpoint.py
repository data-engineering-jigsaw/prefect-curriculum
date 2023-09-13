import requests
import pandas as pd
from prefect import flow, task

@task
def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()

@task
def write_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('./data/receipts.csv')

@flow
def get_and_write_data(name):
    receipts = find_receipts(name)
    df = write_to_csv(receipts)
    return df

name = 'HONDURAS MAYA CAFE & BAR LLC'
get_and_write_data(name)