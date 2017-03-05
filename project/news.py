import requests


"""
#http://api.npr.org/query?searchTerm=abortion&dateType=story&output=NPRML&apiKey=MDI4MDI3OTQzMDE0ODg2NjMzMzFlZTBmZg000
npr_params = {'searchTerm':'abortion','dateType':'story','output':'output.JSON','apiKey':'MDI4MDI3OTQzMDE0ODg2NjMzMzFlZTBmZg000'}
npr = requests.get('http://api.npr.org/query')
print npr.json()
"""


"""
"""
def getNews(query):
    news = []

    #NYT
    payload = {'api_key':'2eca7df7c2204c69b0f72c2c7f62afc3','q':query}
    nyt = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json',params=payload)
    nyt_response = nyt.json()['response']['docs']

    #put NYT into dict to return
    for article in nyt_response:
        source = {}
        source['headline'] = article['headline']['main']
        source['url'] = article['web_url']
        source['date'] = article['pub_date']
        source['source'] = 'New York Times'
        news.append(source)

    return news

def main():
    pass

if __name__ == "__main__":
    main()
