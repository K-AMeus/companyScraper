import time
from bs4 import BeautifulSoup
import requests
import json
import re

def fetch_and_parse(url):
    #Fetch and parse the XML content from a URL.
    time.sleep(1)
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'xml')
    else:
        print(f"Failed to fetch the sitemap at {url}. Status code: {response.status_code}")
        return None
    
def searcherr(keyword):

    articles = []
    # Fetch the sitemap
    sitemap_url = 'https://www.err.ee/sitemap'
    main_sitemap  = fetch_and_parse(sitemap_url)

    if main_sitemap:
        sitemap_urls = [url.text for url in main_sitemap.find_all('loc')]

        # Iterating through each sitemap URL
        for sitemap in sitemap_urls:
            parsed_sitemap = fetch_and_parse(sitemap)
            # Determine the type of sitemap based on the url
            type = re.split(r'\d+', sitemap.split('/')[-1])[0]

            if type == "videos":
                # Handle video sitemap
                for element in parsed_sitemap.find_all('url'):
                    loc = element.find('loc').text
                    title = element.find('video:title').text if element.find('video:title') else ''
                    description = element.find('video:description').text if element.find('video:description') else ''
                    tags = [tag.text for tag in element.find_all('video:tag')]
                    date = element.find('video:publication_date').text if element.find('video:publication_date') else ''

                    if (keyword.lower() in title.lower() or keyword.lower() in description.lower() or any(keyword.lower() in tag.lower() for tag in tags)):
                        articles.append({
                            "title": title,
                            "url": loc,
                            "publication_date": date,
                            "description": description
                        })

            elif type == "sitemap":
                # Handle general sitemap
                for element in parsed_sitemap.find_all('url'):
                    loc = element.find('loc').text
                    image_title = element.find('image:title').text if element.find('image:title') else ''
                    date = element.find('lastmod').text if element.find('lastmod') else ''

                    if keyword.lower() in image_title.lower():
                        articles.append({
                            "title": image_title,
                            "url": loc,
                            "publication_date": date,
                            "description": ""
                        })

            elif type == "news":
                # Handle news sitemap
                for element in parsed_sitemap.find_all('url'):
                    loc = element.find('loc').text
                    title = element.find('news:title').text if element.find('news:title') else ''
                    keywords = element.find('news:keywords').text if element.find('news:keywords') else ''
                    date = element.find('news:publication_date').text if element.find('news:publication_date') else ''

                    if keyword.lower() in title.lower() or keyword.lower() in keywords.lower():
                        articles.append({
                            "title": title,
                            "url": loc,
                            "publication_date": date,
                            "description": ""
                        })

    # Convert the list of articles to JSON
    articles_data = {"articles": articles}
    json_data = json.dumps(articles_data, indent=4, ensure_ascii=False)

    return json_data

#print(searcherr('swedbank'))