import urllib.request
import json

def get_content(link):
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        return data
    raise ValueError("Not able to scrape")

if __name__ == "__main__":
    pass

