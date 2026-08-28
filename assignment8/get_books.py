# Task 3: Write a Program to Extract this Data
import json

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)


results = []

try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    library_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(library_url)

    books = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

    for book in books:

        # Find the title of the book
        try:
            title_element = book.find_element(
                By.CSS_SELECTOR,
                "div.cp-search-result-item-info a"
            )
            title = title_element.get_attribute("title").strip()
        except NoSuchElementException:
            print("Could not find the title.")
            title = "Unknown Title"

        # Find the author of the book
        try:
            author_elements = book.find_elements(
                By.CSS_SELECTOR,
                "span.cp-author-link a"
            )
            author = ";".join([author.text.strip() for author in author_elements])

            # If no authors were found, use the default value
            if not author:
                author = "Unknown Author"
        except NoSuchElementException:
            print("Could not find the author.")
            author = "Unknown Author"

        # Find the format and year of the book
        try:
            format_year_element = book.find_element(
                By.CSS_SELECTOR,
                "div.cp-format-info span"
            )
            format_year = format_year_element.text.replace("\u2014", "-").strip()
        except NoSuchElementException:
            print("Could not find the format/year.")
            format_year = "Unknown Format-Year"

        book_data = {
            "Title": title,
            "Author": author,
            "Format-Year": format_year
        }

        results.append(book_data)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(results)

    # Print the DataFrame
    print(df)

    # Task 4: Write out the Data
    # Save the DataFrame to a CSV file
    df.to_csv("get_books.csv", index=False, encoding="utf-8-sig")

    # Save results to a JSON file
    with open("get_books.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4, ensure_ascii=False)

finally:
    driver.quit()
