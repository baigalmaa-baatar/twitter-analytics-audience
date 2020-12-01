from TwitterAPI import TwitterAPI
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import json

consumer_key = ""
consumer_secret = ""
# bearer_token = ""
access_token_key= ""
access_token_secret= ""

api = TwitterAPI(consumer_key,
                 consumer_secret,
#                  bearer_token,
                 access_token_key,
                 access_token_secret)

#Insert the search words:

response = api.request("statuses/filter", {"track": ["Mandalorian", "and", "Grogu"]})
tweets = response.get_iterator()

country_code = []
count = 0

#How many tweets to analyze:200

while count < 200:
    tweet = next(tweets)
    if "place" in tweet and tweet["place"] != None:
        location = tweet["place"]["country_code"]
        country_code.append(location)
        count += 1

#Save results in CSV file
df = pd.DataFrame(country_code)
df.to_csv("coordinates_starwars.csv", index = False)

#Used Tableau to visualize (for its' fine visualitzation)