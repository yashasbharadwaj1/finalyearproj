from sentiment_api.sentiment.y import SeleniumScraper
from sentiment_api.sentiment import mongo_connection

my = mongo_connection.mydata

# after movie there is a space
"""
columns = {"movie ": 1, "url": 1}

query = {
    "movie ": "Pathan"
}
docs = my.find(query, columns)

d = list(docs)
#after movie space is cumpulsory
name = d[0]['movie ']
video_link = d[0]['url']
#print(name,video_link)


query = {
    "movie ": "Cirkus"
}
docs = my.find(query, columns)

d = list(docs)
#after movie space is cumpulsory
name = d[0]['movie ']
video_link = d[0]['url']
#print(name,video_link)

"""
video_link = "https://www.youtube.com/watch?v=eQG6hzmJuwI&t=3s"
name = "kisikibhaikisikijaan"
obj = SeleniumScraper(video_link,name)

scraped = obj.scrape()

cleaned= obj.cleandata()

print(cleaned.head())

