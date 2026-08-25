import csv

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Wait up to 10 seconds for elements to be present
wait = WebDriverWait(driver, 10) 
owasp_url = "https://owasp.org/www-project-top-ten/"
driver.get(owasp_url)
try:
    top_ten_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='OWASP Top Ten 2025']")
        )
    )
    top_ten_link.click()

    top_items = driver.find_elements(
    By.XPATH, 
    "//h3[@id='top-102025-list']/following-sibling::ol[1]/li" 
    )

    for index, item in enumerate(top_items, start=1):
        # Find the <a> tag nested inside <li>
        link_element = item.find_element(By.TAG_NAME, "a")
        
        # Get the visible text (e.g., "A01:2025 - Broken Access Control")
        item_title  = link_element.text.strip()
        
        # Get the URL it points to
        item_href = link_element.get_attribute("href")

        print(f"title: {item_title}, href: {item_href}")

        item_data = {
            "title": item_title,
            "href": item_href
        }
        results.append(item_data)

    with open('owasp_top_10.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        for link in results:
            writer.writerow([link["title"], link["href"]])

except Exception as e:
    print("Exception occurred:", str(e))



