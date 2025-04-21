import requests
from send_email import send_email
#api_key = "ad89b54e0ff342baa73a9add458c47a5"
topic="sports"
url=("https://newsapi.org/v2/"
     f"everything?q={topic}&from=2025-01-20"
     "&sortBy=publishedAt&apiKey=ad89b54e0ff342baa73a9add458c47a5&language=en")

# Made a request
request=requests.get(url=url)

# Get data in a dictionary
content=request.json()

# Itterate over content
body=""
for i in content.get('articles',[])[:10]:
    body=(body+str(i["title"])+"\n"+str(i["description"])+"\n"+str(i["url"])+"\n\n")
body=(""
      "Subject: Today's News "
      "\n"
      +body)
body = body.encode("utf-8")

send_email(body)




