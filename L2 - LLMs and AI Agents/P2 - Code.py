import requests

def fetch_news(api_key):
    url = "https://newsapi.org/v2/everything"
    parameters = {
        'q': 'technology',  # Query term. Change this as needed.
        'pageSize': 5,  # Limit the number of articles
        'apiKey': api_key
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = 'api_here'
news_data = fetch_news(api_key)
if news_data:
    print(news_data)  # You can process this data further
else:
    print("Failed to retrieve news")
