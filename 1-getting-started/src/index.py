import requests
from prefect import flow, task

@task
def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()[:1]

@flow
def get_data(url):
    receipts = find_receipts(url)
    return receipts

name = 'HONDURAS MAYA CAFE & BAR LLC'
print(get_data(name))