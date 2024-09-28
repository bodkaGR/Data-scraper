from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_news_titles():
    titles = driver.find_elements(By.XPATH, "//li[@class='all-news__list all-news__list_image']/a")
    return [title.text for title in titles]

def click_next():
    try:
        next_button = driver.find_element(By.XPATH, "//a[@class='all-news__button_forward']/span[contains(text(), 'Далее')]")
        next_button.click()
        time.sleep(10)
        return True
    except:
        return False


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    url = 'https://pestrecy-rt.ru/news/tag/list/specoperaciia/'

    driver.get(url)

    all_titles = [[] for _ in range(5)]

    for i in range(5):
        titles = get_news_titles()
        all_titles[i].extend(titles)

        if not click_next():
            break

    driver.quit()

    for spec_titles in all_titles:
        print(spec_titles)

