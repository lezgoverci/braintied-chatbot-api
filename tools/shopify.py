import requests
from actions.shopify import get_products
import os

access_token = os.getenv('CHATBOT_SHOPIFY_STOREFRONT_PUBLIC_ACCESS_TOKEN')
store= os.getenv('CHATBOT_SHOPIFY_STORE_URI')

def fetch_products(count):
    query = get_products(count)
    url = f'https://{store}/api/2023-10/graphql.json'
    headers = {
        'Content-Type': 'application/graphql',
        'X-Shopify-Storefront-Access-Token': access_token
    }
    response = requests.post(url, headers=headers, data=query)
    return response.json()