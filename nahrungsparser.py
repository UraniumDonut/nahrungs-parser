from requests_html import HTMLSession
import time, requests
print("nahrungsparser gestartet")


urlsp6 = "aubauen hier"+"extra"

nodes = requests.get("https://www.todayonline.com/api/v3/news_feed/7")\
        .json()["nodes"]
for node in nodes:
    print(node["node"]["title"])