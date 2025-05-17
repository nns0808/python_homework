from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

options = Options()
options.add_argument("--headless=new")  
driver = webdriver.Chrome(options=options)

driver.get("https://owasp.org/www-project-top-ten/")

try:
    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "2021") and contains(@href, "A0")]'))
    )

    links = driver.find_elements(By.XPATH, '//a[contains(@href, "2021") and contains(@href, "A0")]')

    results = []
    for link in links:
        title = link.text.strip()
        href = link.get_attribute("href")
        if title and href:
            results.append({"Title": title, "Link": href})

    
    print(f"Found {len(results)} vulnerabilities.")
    for r in results:
        print(r)

    # Save to CSV
    df = pd.DataFrame(results)
    os.makedirs("assignment9", exist_ok=True)
    df.to_csv("assignment9/owasp_top_10.csv", index=False)

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()


