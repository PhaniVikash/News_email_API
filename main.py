import requests

api_key = "ad89b54e0ff342baa73a9add458c47a5"
url=("https://newsapi.org/v2/"
     "everything?q=tesla&from=20"
     "25-01-20&sortBy=publishedAt&apiKey=ad89b54e0ff342baa73a9add458c47a5")

# Made a request
request=requests.get(url)

# Get data in a dictionary
content=request.json()

# Itterate over content
for i in content["articles"]:
    print(i["title"])
    print(i["description"])

