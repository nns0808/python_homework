from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


time.sleep(3)

results = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")


for index, item in enumerate(results, start=1):
    print(f"\nResult {index}:")
    print(item.text)
    print("-" * 40)

search_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")


# Empty 
results = []


for item in search_items:
    try:
        title_element = item.find_element(By.CSS_SELECTOR, "span.title-content")
        title = title_element.text.strip()

        url_element = item.find_element(By.CSS_SELECTOR, "span.title-content")

        url = url_element.get_attribute("href")

        result_dict = {
            "title": title,
            "url": url
        }

        results.append(result_dict)
    except Exception as e:
        print(f"Skipping item due to error: {e}")


for res in results:
    print(res)



for item in search_items:
    try:
        # Title
        title_element = item.find_element(By.CSS_SELECTOR, "span.title-content")
        title = title_element.text.strip()
    except:
        title = "N/A"

    try:
        # Authors 
        author_elements = item.find_elements(By.CSS_SELECTOR, "div.author a")
        authors = [a.text.strip() for a in author_elements]
        author_text = "; ".join(authors) if authors else "N/A"
    except:
        author_text = "N/A"

    try:
        # Format and Year
        format_year_element = item.find_element(By.CSS_SELECTOR, "div.cp-format span")
        format_year = format_year_element.text.strip()
    except:
        format_year = "N/A"

    # Compose dictionary
    book_data = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }

    results.append(book_data)


for res in results:
    print(res)


driver.quit()


import pandas as pd


data = [
    {'Title': 'Real-World Spanish: The Conversation Learning System', 'Author': 'John Doe', 'Format-Year': 'Paperback 2020'},
    {'Title': 'Learning Spanish-beginner I', 'Author': 'Jane Smith', 'Format-Year': 'Ebook 2019'},
    {'Title': '100 Facts About Learning Spanish', 'Author': 'Mary Johnson', 'Format-Year': 'Hardcover 2021'},
    {'Title': '100 Facts About Learning Spanish', 'Author': 'Robert Brown', 'Format-Year': 'Paperback 2022'},
    {'Title': 'The Ultimate Learning Spanish Blueprint - 10 Essential Steps', 'Author': 'Alice White', 'Format-Year': 'Ebook 2018'}
]


df = pd.DataFrame(data)

print(df)



