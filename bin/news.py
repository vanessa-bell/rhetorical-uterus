import requests

#nyt_params = {'api_key':'2eca7df7c2204c69b0f72c2c7f62afc3','q':'abortion'}
#nyt = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json',params=nyt_params)
#nyt_response = nyt.json()['response']['docs']
#for article in nyt_response:
#    print article['headline']['main']
#    print ''


#http://api.npr.org/query?searchTerm=abortion&dateType=story&output=NPRML&apiKey=MDI4MDI3OTQzMDE0ODg2NjMzMzFlZTBmZg000
npr_params = {'searchTerm':'abortion','dateType':'story','output':'output.JSON','apiKey':'MDI4MDI3OTQzMDE0ODg2NjMzMzFlZTBmZg000'}
npr = requests.get('http://api.npr.org/query')

print npr.json()


