import requests
from bs4 import BeautifulSoup

def get_titles(page, base_url):
    url = f"{base_url}{page}"

    response = requests.get(url)

    if response.status_code == 404:
        print(f"Page {page} does not exist. Stopping.")
        return None
    return response.content


def parse_news(content):
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all(class_="all-news__list_text-container")

    for news in links:
        parsed = news.text.strip()
        if parsed:
            all_titles.append(parsed)
            print(parsed)



if __name__ == "__main__":
    all_titles = []

    base_url = "https://pestrecy-rt.ru/news/tag/list/specoperaciia/page/"

    page = 1

    while True:
        data = get_titles(page, base_url)
        if data is None:
            break
        parse_news(data)
        page += 1


