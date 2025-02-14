import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from flask import request, jsonify 
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from app import create_app

app = create_app()
CORS(app)  # Allow all origins by default

@app.route('/api/scrape', methods=['POST'])
def scrape_page():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(data['url'])
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        #description = soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else "No description found"
        h4_arr = soup.find_all("h4")

        h4_text = []
        for h4 in h4_arr:
            h4_text.append(h4.text+"\n")


        return jsonify({"title": title, "description": h4_text}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()

    if not data or 'query' not in data:
        return jsonify({"error": "Query is required"}), 400

    query = data['query']
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('CX_KEY')          

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cx).execute()

        return jsonify(res), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')